#!/usr/bin/env python3

from flask import Flask, request, jsonify, g
from validate_docbr import CPF
import sqlite3

cpf = CPF()
app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.config["DEBUG"] = False

DB_URL = "database/dados.db"


@app.before_request
def before_request():
    global conn
    conn = sqlite3.connect(DB_URL)
    g.conn = conn


@app.teardown_request
def after_request(exception):
    if g.conn is not None:
        g.conn.close()


def query_dict(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)

    response_dict = [
            {
                "nome": row[0],
                "cpf": cpf.mask(row[1]),
                "estado": row[2],
                "cidade": row[3]

        } for row in cursor.fetchall()
    ]

    for obj in response_dict:
        return obj


@app.route('/', methods=['GET'])
@app.route('/api', methods=['GET'])
def _cpf():
    parameters = request.args

    if not parameters.get("cpf"):
        return jsonify(
            status=400,
            #remote_addr=request.remote_addr,
            data="Parametros invalidos. Tente: /api?cpf=<cpf>"
        )

    if not cpf.validate(parameters.get("cpf")):
        return jsonify(
            status=404,
            #remote_addr=request.remote_addr,
            data="CPF invalido."
        )

    query = """
        SELECT nome, cpf, estado, cidade
        FROM database
        WHERE "cpf" LIKE "{}";
        """.format(parameters.get("cpf"))

    response_dict = query_dict(g.conn, query)
    if response_dict is not None:
        return jsonify(
            status=200,
            #remote_addr=request.remote_addr,
            data=response_dict,
        )

    return jsonify(
        status=204,
        #remote_addr=request.remote_addr,
        data="Nao encontrado na nossa base de dados."
    )


app.run(
    host = "0.0.0.0",
    threaded = True
);
