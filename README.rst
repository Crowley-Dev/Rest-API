API Rest - Flask
================

- **próxima atualização**: *××/××/××××*
- **mudanças na próxima atualização**:
   - *sistema de autenticação de token*
   - *cada token terá um tempo de uso (7d, 15d, 30d)*
   - *sistema de blacklist, caso o usuário faça muitas requisição em pouco tempo*

- **informo que**: *o banco de dados usado nesse projeto é totalmente fictício.*


dependências
------------

- `flask`_
- `validate-docbr`_

.. _flask: https://github.com/pallets/flask
.. _validate-docbr: https://github.com/alvarofpp/validate-docbr


instalação
----------

.. code-block:: powershell

	git clone https://github.com/Crowley-Dev/Rest-API


um exemplo simples de requisição
--------------------------------

.. code-block:: python

	import requests


	url = "http://0.0.0.0:5000/api?cpf={}"

	resp = requests.request(
	    method = "GET",
	    url = url.format("11712979710"),
	    headers = {
	        "Content-Type": "application/json"
	    }

	); print(resp.text)


response
--------

.. code-block:: json

	{
	  "data": {
	    "cidade": "TEIXEIRA DE FREITAS",
	    "cpf": "11712979710",
	    "estado": "BA",
	    "nome": "BRUNA ALMEIDA LOVO"
	  },
	  "status": 200
	}
