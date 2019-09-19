#!/Users/tulio/Developer/Localiza/venv-api-pdc/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/checklistdesativacao/parametros', methods=['GET'])
def obterParametros():
    
    parametros = {
        "opstatus": 0,
        "TipoOrigemConfiguracao": "Agencia",
        "NumeroMaximoTentativasSubidaChecklist": 3,
        "TipoOrigemFornecedor": "Agencia",
        "LimiteKMSeminovos": 100,
        "KmMaximoRac": 300000,
        "TipoOrigemCentroManutencao": "CentroManutencao",
        "TipoOrigemLoja": "Loja",
        "MedidaPadraoTWI": 290,
        "KmMaximoGF": 100,
        "TipoOrigemAgencia": "Agencia",
        "PatrimonioConfiguracao": "123456",
        "OrigemConfiguracao": "123456",
        "LimiteTextoComentario": 30,
        "SenhaConfiguracao": "444",
        "LimiteFotoPorItem": 3,
        "httpStatusCode": 200
        }

    return jsonify(parametros)

@app.route('/api/v1/checklistdesativacao/RealizarLogin', methods=['POST'])
def realizarLogin():
    login = {
        "Sucesso": True,
        "Mensagem": "Login efetuado com sucesso",
        "Nome": "Nome de teste"
    }
    return jsonify(login)


@app.route('/api/v1/configuracao/vinculardispositivoagencia', methods=['POST'])
def vincularDispositivo():
    vincularDispositivo = {
                            "AgenciaValida": "false",
                            "ConflitoPatrimonio": "true",
                            "ConflitoDispositivo": "true",
                            "Sucesso": "true",
                            "RetornoAPI": "",
                            "opstatus": 0,
                            "Data": "0001-01-01T00:00:00",
                            "Mensagem": "O patrimônio 10101 já está vinculado a um dispositivo da agência ACBHZ .",
                            "httpStatusCode": 200
                            }
    return jsonify(vincularDispositivo)


@app.route('/api/v1/configuracao/vinculardispositivofornecedor', methods=['POST'])
def vincularDispositivoFornecedor():
    fornecedor ={
                    "AgenciaValida": True,
                    "ConflitoPatrimonio": False,
                    "ConflitoDispositivo": True,
                    "Sucesso": True,
                    "RetornoAPI": "",
                    "Data": "0001-01-01T00:00:00",
                    "Mensagem": "O patrimônio 10101 já está vinculado a um dispositivo da agência ACBHZ .",
                    "opstatus": 0,
                    "httpStatusCode": 200
                }
    return jsonify(fornecedor)


@app.route('/api/v1/configuracao/vinculardispositivoloja', methods=['POST'])
def vincularDispositivoSN():
    sn ={
                    "AgenciaValida": True,
                    "ConflitoPatrimonio": False,
                    "ConflitoDispositivo": True,
                    "Sucesso": True,
                    "RetornoAPI": "",
                    "Data": "0001-01-01T00:00:00",
                    "Mensagem": "O patrimônio 10101 já está vinculado a um dispositivo da agência ACBHZ .",
                    "opstatus": 0,
                    "httpStatusCode": 200
                }
    return jsonify(sn)


@app.route('/api/v1/configuracao/vinculardispositivocentromanutencao', methods=['POST'])
def vincularDispositivoCM():
    cm ={
                    "AgenciaValida": True,
                    "ConflitoPatrimonio": False,
                    "ConflitoDispositivo": True,
                    "Sucesso": True,
                    "RetornoAPI": "",
                    "Data": "0001-01-01T00:00:00",
                    "Mensagem": "O patrimônio 10101 já está vinculado a um dispositivo da agência ACBHZ .",
                    "opstatus": 0,
                    "httpStatusCode": 200
                }
    return jsonify(cm)


@app.route('/api/v1/checklistdesativacao/ValidarLoginFornecedorGFRAC', methods=['POST'])
def validarLoginFornecedorGFRAC():
    login = {
        "TipoUsuario": "teste",
        "NomeReduzido": "Tulio Cesar",
        "opstatus": 0,
        "SeEhValido": True,
        "Mensagem": "",
        "httpStatusCode": 200
        }
    return jsonify(login)


@app.route('/api/v1/checklistdesativacao/ValidarPlaca', methods=['POST'])
def validarPlaca():
    response = {
        "PlacaValida": True,
        "CodigoCliente": "123123123",
        "Mensagem": "O carro esta na agencia ACBHZ",
        "placa": "PZK7724",
        "opstatus": 0,
        "httpStatusCode": 200
        }

    return jsonify(response)


@app.route('/api/v1/checklistdesativacao/BuscaCabecalhoPorPlaca', methods=['POST'])
def buscaCabecalhoPorPlaca():
    cab = {
        "Modelo": "HONDA CIVIC TURING 2019",
        "Cor": "PRETO",
        "TipoVenda": "S",
        "opstatus": 0,
        "TipoFrota": "2",
        "httpStatusCode": 200
    }
    return jsonify(cab)

@app.route('/api/v1/checklistdesativacao/ValidarExibicaoMenuInicial', methods=['POST'])
def validarExibicaoMenuInicial():
    response = {
        "ItensMenuInicial": {
            "ExibirBotaoResumoChecklist": True,
            "ExibirBotaoEntregaERecebimento": True, 
            "ExibirTelaMenuInicial": True,
            "ExibirBotaoChecklist": True,
            "ExibirBotaoProtocolo": True
        },
        "Sucesso": True,
        "opstatus": 0,
        "Mensagem": "Dispositivo não encontrado.",
        "httpStatusCode": 200
        }
    return jsonify(response)


@app.route('/api/v1/checklistdesativacao/ListagemChecklistPorPlaca', methods=['GET'])
def listagemChecklistPorPlaca():
    response = {
        "Sucesso": True,
        "ListaChecklist": [{
            "CodigoTipoChecklist": "3",
            "SS": "2313ZH/40",
            "CodigoExecucao": "",
            "CodigoStatusChecklist": "",
            "HabilitarAssinatura": False,
            "HabilitarEdicao": False,
            "CodigoChecklist": "140123",
            "ResponsavelExecucao": "PEDRO EDUARDO RIBEIRO DE ARAUJO",
            "TipoChecklist": "Conferencia",
            "HabilitarNovo": False,
            "DataExecucao": "2018-09-06T15:33:28",
            "Placa": "PZY6185",
            "HabilitarVisualizacaoPDF": False,
            "HabilitarEmail": True,
            "StatusChecklist": "Finalizado"
            },
            {
            "CodigoTipoChecklist": "4",
            "SS": "2313ZH/40",
            "CodigoExecucao": "",
            "CodigoStatusChecklist": "",
            "HabilitarAssinatura": False,
            "HabilitarEdicao": False,
            "CodigoChecklist": "153789",
            "ResponsavelExecucao": "ISAIAS REIS BUENO",
            "TipoChecklist": "Qualidade",
            "HabilitarNovo": False,
            "DataExecucao": "2018-09-24T11:23:05",
            "Placa": "PZY6185",
            "HabilitarVisualizacaoPDF": False,
            "HabilitarEmail": False,
            "StatusChecklist": "Finalizado"
            },
            {   
            "CodigoTipoChecklist": "4",
            "SS": "2313ZH/40",
            "CodigoExecucao": "",
            "CodigoStatusChecklist": "",
            "HabilitarAssinatura": False,
            "HabilitarEdicao": False,
            "CodigoChecklist": "0",
            "ResponsavelExecucao": "TESTE",
            "TipoChecklist": "Qualidade",
            "HabilitarNovo": False,
            "DataExecucao": "2019-08-28T13:43:24",
            "Placa": "PZY6185",
            "HabilitarVisualizacaoPDF": False,
            "HabilitarEmail": False,
            "StatusChecklist": "0"
        }],
        
        "HabilitarNovo": True,
        "opstatus": 0,
        "Mensagem": "",
        "httpStatusCode": 200
        }

    return jsonify(response)

@app.route('/api/v1/checklistdesativacao/BuscarChecklistCliente', methods=['POST','GET'])
def BuscarChecklistCliente():
    response = {
        "ResumoChecklist": [{
            "cabecalho": {
                "SS": "23NMV4/40",
                "frota": "2",
                "dataExecucao": "1/1/0001 12:00:00 AM",
                "responsavelExecucao": "",
                "cor": "BRANCO ASPEN",
                "modelo": "NEW MARCH S 1.0 12V FLEX 4P C/AR",
                "agenciaExecucao": "",
                "placa": "QNS6982"
            },
            "dadosCarro": {
              "Blindado": False,  
              "CertificadoBlindagem": False,
              "Chassi": "94DFFUK13JB204528",  
              "ChassiConferido": False,
              "ChassiOxidado": False,
              "ChassiRasgado": False,
              "Combustivel": "6",
              "Comentario": "",
              "CompradorFinal": True,
              "ConfirmacaoGarantia": True,
              "ConfirmacaoGarantiaItem": "13299",
              "ConfirmacaoGarantiaParte": "4954",
              "Cor": False,
              "DT": False,
              "EhRac": True,
              "ExcessivamenteSujo": False,
              "ExcessivamenteSujoItem": "10818",
              "ExcessivamenteSujoParte": "4954",
              "Garantia": "SIM",
              "Idade": "602",
              "KitGNV": False,
              "Km": "26879",
              "KmUltimaRevisaoRac": "",
              "ListaFotoConfirmacaoGarantia": [],
              "ListaFotoExcessivamenteSujo": [],
              "NotaDez": False,
              "PT": False,
              "QuantidadeCilindro": "0",
              "Revenda": False,
              "RevendaDesabilitado": False,
              "Revisao": "0Km"}
            ,
        #     "partes": [{
        #     "parte": "Dianteira",
        #     "habilitadoEdicao": True,
        #     "listaItemResposta": [{
        #         "descricaoItem": "Bateria",
        #         "estaOk": None,
        #         "codigoModelo": 3733,
        #         "item": {
        #             "obrigatorio": True,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Descarregado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8028,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3734,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8029,
        #                 "descricao": "Recarregar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8030,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8031,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3735,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8032,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8033,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3736,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8034,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Capo",
        #         "estaOk": True,
        #         "codigoModelo": 3737,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Adesivado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8035,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3738,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8036,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8037,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8038,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3739,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8039,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8040,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8041,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3740,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8042,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8043,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8044,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3741,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8045,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8046,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3742,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8047,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8048,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3743,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8049,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 8050,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3744,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8051,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Abre/Fecha",
        #             "valorProblema": "",
        #             "codigoPergunta": 8052,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3745,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8053,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8054,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8055,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3746,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8056,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8057,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3747,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8058,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8059,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3748,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8060,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8061,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 8062,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3749,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8063,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8064,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8065,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3750,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8066,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8067,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Carter Motor",
        #         "estaOk": True,
        #         "codigoModelo": 3751,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8068,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3752,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8069,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8070,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8071,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3753,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8072,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8073,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3754,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8074,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8075,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Trincado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8076,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3755,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8077,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8078,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Vazamento",
        #             "valorProblema": "",
        #             "codigoPergunta": 8079,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3756,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8080,
        #                 "descricao": "Verificar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Escape inter/tras",
        #         "estaOk": True,
        #         "codigoModelo": 3757,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8081,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3758,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8082,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8083,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8084,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3759,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8085,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8086,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3760,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8087,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8088,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Trincado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8089,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3761,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8090,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8091,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Vazamento",
        #             "valorProblema": "",
        #             "codigoPergunta": 8092,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3762,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8093,
        #                 "descricao": "Verificar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Farol Dir",
        #         "estaOk": True,
        #         "codigoModelo": 3763,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8094,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3764,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8095,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Infiltração",
        #             "valorProblema": "",
        #             "codigoPergunta": 8096,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3765,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8097,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8098,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8099,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3766,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8100,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8101,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3767,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8102,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8103,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8104,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3768,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8105,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8106,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8107,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3769,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8108,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8109,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Trincado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8110,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3770,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8111,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8112,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Farol Esq",
        #         "estaOk": True,
        #         "codigoModelo": 3771,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8113,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3772,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8114,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Infiltração",
        #             "valorProblema": "",
        #             "codigoPergunta": 8115,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3773,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8116,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8117,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8118,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3774,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8119,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8120,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3775,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8121,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8122,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8123,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3776,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8124,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8125,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8126,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3777,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8127,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8128,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Trincado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8129,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3778,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8130,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8131,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Farol Milha Dir",
        #         "estaOk": True,
        #         "codigoModelo": 3779,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8132,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3780,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8133,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Infiltração",
        #             "valorProblema": "",
        #             "codigoPergunta": 8134,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3781,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8135,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8136,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8137,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3782,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8138,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8139,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3783,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8140,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8141,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8142,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3784,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8143,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8144,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8145,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3785,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8146,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8147,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Trincado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8148,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3786,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8149,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8150,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Farol Milha Esq",
        #         "estaOk": True,
        #         "codigoModelo": 3787,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8151,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3788,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8152,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Infiltração",
        #             "valorProblema": "",
        #             "codigoPergunta": 8153,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3789,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8154,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8155,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8156,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3790,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8157,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8158,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3791,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8159,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8160,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8161,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3792,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8162,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8163,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8164,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3793,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8165,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8166,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Trincado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8167,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3794,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8168,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8169,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Grande Dianteira",
        #         "estaOk": True,
        #         "codigoModelo": 3795,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8170,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3796,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8171,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8172,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8173,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3797,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8174,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8175,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8176,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3798,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8177,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8178,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3799,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8179,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8180,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8181,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3800,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8182,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8183,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3801,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8184,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8185,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3802,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8186,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8187,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8188,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3803,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8189,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8190,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8191,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3804,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8192,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8193,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Insulfilm Para Brisa",
        #         "estaOk": True,
        #         "codigoModelo": 3805,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Avariado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8194,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3806,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8195,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8196,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8197,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3807,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8198,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Limpador/Palheta",
        #         "estaOk": True,
        #         "codigoModelo": 3808,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8199,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3809,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8200,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8201,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3810,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8202,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8203,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3811,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8204,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8205,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Ressecado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8206,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3812,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8207,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Motor",
        #         "estaOk": None,
        #         "codigoModelo": 3813,
        #         "item": {
        #             "obrigatorio": True,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Barulho",
        #             "valorProblema": "",
        #             "codigoPergunta": 8208,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3814,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8209,
        #                 "descricao": "Verificar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Falhando",
        #             "valorProblema": "",
        #             "codigoPergunta": 8210,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3815,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8211,
        #                 "descricao": "Verificar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Funciona",
        #             "valorProblema": "",
        #             "codigoPergunta": 8212,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3816,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8213,
        #                 "descricao": "Verificar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8214,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3817,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8215,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Vazamento",
        #             "valorProblema": "",
        #             "codigoPergunta": 8216,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3818,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8217,
        #                 "descricao": "Verificar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Painel Dianteiro",
        #         "estaOk": True,
        #         "codigoModelo": 3820,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Adesivado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8219,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3821,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8220,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8221,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8222,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3822,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8223,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8224,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8225,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3823,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8226,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8227,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8228,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3824,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8229,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8230,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3825,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8231,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8232,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3826,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8233,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8234,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3827,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8235,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8236,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3828,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8237,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8238,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 8239,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3829,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8240,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8241,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8242,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3830,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8243,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8244,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Para Brisa",
        #         "estaOk": True,
        #         "codigoModelo": 3831,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8245,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3832,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8246,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8247,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3833,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8248,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8249,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8250,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3834,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8251,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8252,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8253,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3835,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8254,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8255,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Para Choque Diant",
        #         "estaOk": True,
        #         "codigoModelo": 3836,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8256,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3837,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8257,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8258,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8259,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3838,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8260,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8261,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3839,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8262,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8263,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3840,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8264,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8265,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3841,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8266,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8267,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3842,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8268,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8269,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3843,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8270,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8271,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8272,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3844,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8273,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8274,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 13291,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 5370,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 13292,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 13293,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8275,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3845,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8276,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8277,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Protetor Carter",
        #         "estaOk": True,
        #         "codigoModelo": 3846,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8278,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3847,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8279,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8280,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8281,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3848,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8282,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8283,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3849,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8284,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8285,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3850,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8286,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8287,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Radiador",
        #         "estaOk": True,
        #         "codigoModelo": 3851,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8288,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3852,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8289,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8290,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8291,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3853,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8292,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8293,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3854,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8294,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8295,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Trincado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8296,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3855,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8297,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8298,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Vazamento",
        #             "valorProblema": "",
        #             "codigoPergunta": 8299,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3856,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8300,
        #                 "descricao": "Verificar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Travessa Radiador",
        #         "estaOk": True,
        #         "codigoModelo": 3863,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Adesivado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8314,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3864,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8315,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8316,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8317,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3865,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8318,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8319,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8320,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3866,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8321,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8322,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3867,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8323,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8324,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3868,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8325,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8326,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3869,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8327,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8328,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3870,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8329,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8330,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 8331,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3871,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8332,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8333,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8334,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3872,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8335,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8336,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Tubo/Catalisador",
        #         "estaOk": True,
        #         "codigoModelo": 3873,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8337,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3874,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8338,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8339,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8340,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3875,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8341,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8342,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3876,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8343,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8344,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Trincado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8345,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3877,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8346,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8347,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Vazamento",
        #             "valorProblema": "",
        #             "codigoPergunta": 8348,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3878,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8349,
        #                 "descricao": "Verificar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Outros",
        #         "estaOk": True,
        #         "codigoModelo": 3819,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 2,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8218,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 5369,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 13290,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }]
        #     }],
        #     "ehParteDesenho": True,
        #     "codigoParte": 3732
        # }, {
        #     "parte": "Dianteira Direita",
        #     "habilitadoEdicao": True,
        #     "listaItemResposta": [{
        #         "descricaoItem": "Caixa de Ar Direita",
        #         "estaOk": True,
        #         "codigoModelo": 3885,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Adesivado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8360,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3886,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8361,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8362,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8363,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3887,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8364,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8365,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8366,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3888,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8367,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8368,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8369,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3889,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8370,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8371,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3890,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8372,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 8373,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3891,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8374,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8375,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8376,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3892,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8377,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8378,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3893,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8379,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8380,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3894,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8381,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8382,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 8383,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3895,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8384,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8385,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8386,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3896,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8387,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8388,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Caixa de Roda DD",
        #         "estaOk": True,
        #         "codigoModelo": 3897,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8389,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3898,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8390,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8391,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8392,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3899,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8393,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8394,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8395,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3900,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8396,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8397,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3901,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8398,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 8399,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3902,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8400,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8401,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8402,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3903,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8403,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8404,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3904,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8405,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8406,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3905,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8407,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8408,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 8409,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3906,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8410,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8411,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8412,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3907,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8413,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8414,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Calota DD",
        #         "estaOk": True,
        #         "codigoModelo": 3908,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8415,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3909,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8416,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8417,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8418,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3910,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8419,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8420,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8421,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3911,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8422,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8423,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8433,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3915,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8434,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8424,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3912,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8425,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8426,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8427,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3913,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8428,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8429,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8430,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3914,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8431,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8432,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Coluna Dir",
        #         "estaOk": True,
        #         "codigoModelo": 3916,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Adesivado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8435,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3917,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8436,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8437,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8438,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3918,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8439,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8440,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8441,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3919,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8442,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8443,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8444,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3920,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8445,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8446,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3921,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8447,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 8448,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3922,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8449,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8450,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8451,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3923,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8452,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8453,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3924,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8454,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8455,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3925,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8456,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8457,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 8458,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3926,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8459,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8460,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8461,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3927,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8462,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8463,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Entrada de Porta DD",
        #         "estaOk": True,
        #         "codigoModelo": 3928,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8464,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3929,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8465,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8466,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8467,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3930,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8468,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8469,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8470,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3931,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8471,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8472,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3932,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8473,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 8474,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3933,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8475,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8476,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8477,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3934,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8478,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8479,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3935,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8480,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8481,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3936,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8482,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8483,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 8484,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3937,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8485,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8486,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8487,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3938,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8488,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8489,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Forro de Porta DD",
        #         "estaOk": True,
        #         "codigoModelo": 3939,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8490,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3940,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8491,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8492,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8493,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3941,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8494,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8495,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desfiado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8496,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3942,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8497,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8498,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8499,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3943,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8500,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8501,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3944,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8502,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8503,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8504,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3945,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8505,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8506,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8507,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3946,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8508,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8509,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3947,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8510,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8511,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 8512,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3948,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8513,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8514,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Friso/Borrachão Dir",
        #         "estaOk": True,
        #         "codigoModelo": 3949,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Avariado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8515,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3950,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8516,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8517,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desalinhado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8518,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3951,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8519,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8520,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8521,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3952,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8522,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8523,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3953,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8524,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 8525,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3954,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8526,
        #                 "descricao": "Fixar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8527,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Guarnição DD",
        #         "estaOk": True,
        #         "codigoModelo": 3955,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8528,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3956,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8529,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8530,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3957,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8531,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8532,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8533,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3958,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8534,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8535,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3959,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8536,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8537,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3960,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8538,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8539,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8540,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3961,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8541,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 8542,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3962,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8543,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8544,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Insulfilm DD",
        #         "estaOk": True,
        #         "codigoModelo": 3963,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Avariado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8545,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3964,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8546,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8547,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8548,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3965,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8549,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Maçaneta DD",
        #         "estaOk": True,
        #         "codigoModelo": 3966,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8550,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3967,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8551,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8552,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3968,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8553,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Abre",
        #             "valorProblema": "",
        #             "codigoPergunta": 8554,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3969,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8555,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8556,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8557,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3970,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8558,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8559,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3971,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8560,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8561,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8562,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3972,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8563,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8564,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 8565,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3973,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8566,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8567,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8568,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3974,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8569,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8570,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Para Barro Dir",
        #         "estaOk": True,
        #         "codigoModelo": 3976,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8572,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3977,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8573,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8574,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8575,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3978,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8576,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8577,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8578,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3979,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8579,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8580,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3980,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8581,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8582,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8583,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3981,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8584,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8585,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3982,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8586,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8587,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Para Lama Dir",
        #         "estaOk": True,
        #         "codigoModelo": 3983,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Adesivado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8588,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3984,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8589,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8590,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8591,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3985,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8592,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8593,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8594,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3986,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8595,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8596,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8597,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3987,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8598,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8599,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3988,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8600,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 8601,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3989,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8602,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8603,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8604,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3990,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8605,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8606,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3991,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8607,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8608,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3992,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8609,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8610,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 8611,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3993,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8612,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8613,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8614,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3994,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8615,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8616,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Porta DD",
        #         "estaOk": None,
        #         "codigoModelo": 3995,
        #         "item": {
        #             "obrigatorio": True,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Adesivado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8617,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3996,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8618,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8619,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8620,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3997,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8621,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8622,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8623,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3998,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8624,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8625,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8626,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3999,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8627,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8628,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4000,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8629,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 8630,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4001,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8631,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8632,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8633,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4002,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8634,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8635,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4003,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8636,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8637,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4004,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8638,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8639,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 8640,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4005,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8641,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8642,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8643,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4006,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8644,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8645,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Retrovisor DD",
        #         "estaOk": True,
        #         "codigoModelo": 4007,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8646,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4008,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8647,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8648,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4009,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8649,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Abre",
        #             "valorProblema": "",
        #             "codigoPergunta": 8650,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4010,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8651,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8652,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8653,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4011,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8654,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8655,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4012,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8656,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8657,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8658,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4013,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8659,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8660,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 8661,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4014,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8662,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8663,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8664,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4015,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8665,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8666,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Roda DD",
        #         "estaOk": True,
        #         "codigoModelo": 4016,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [{
        #                 "codigo": 4017,
        #                 "descricao": "Modelo",
        #                 "obrigatorio": False,
        #                 "visivel": True,
        #                 "ordem": 0,
        #                 "listaResposta": [{
        #                     "descricao": "Ferro",
        #                     "valor": "",
        #                     "codigoPergunta": 8667,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Liga Leve",
        #                     "valor": "",
        #                     "codigoPergunta": 8668,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }]
        #             }],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8669,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4025,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8685,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 13295,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8672,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4018,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8670,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8671,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8674,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4019,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8673,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8676,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4020,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8675,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8678,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4021,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8677,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8680,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4022,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8679,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 8682,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4023,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8681,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8684,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4024,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8683,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Vidro Porta DD",
        #         "estaOk": True,
        #         "codigoModelo": 4026,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8686,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4027,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8687,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8688,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4028,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8689,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8690,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8691,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4029,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8692,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8693,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8694,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4030,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8695,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8696,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Vidro Retrovisor DD",
        #         "estaOk": True,
        #         "codigoModelo": 4031,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8697,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4032,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8698,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8699,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4033,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8700,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8701,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4034,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8702,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8703,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4035,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8704,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8705,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4036,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8706,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8707,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Outros",
        #         "estaOk": True,
        #         "codigoModelo": 3975,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 2,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8571,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 5371,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 13294,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }]
        #     }],
        #     "ehParteDesenho": True,
        #     "codigoParte": 3879
        # }, {
        #     "parte": "Dianteira Esquerda",
        #     "habilitadoEdicao": True,
        #     "listaItemResposta": [{
        #         "descricaoItem": "Caixa de Ar Esquerda",
        #         "estaOk": True,
        #         "codigoModelo": 4043,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Adesivado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8718,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4044,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8719,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8720,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8721,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4045,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8722,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8723,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8724,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4046,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8725,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8726,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8727,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4047,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8728,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8729,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4048,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8730,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 8731,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4049,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8732,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8733,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8734,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4050,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8735,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8736,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4051,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8737,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8738,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4052,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8739,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8740,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 8741,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4053,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8742,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8743,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8744,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4054,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8745,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8746,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Caixa de Roda DE",
        #         "estaOk": True,
        #         "codigoModelo": 4055,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8747,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4056,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8748,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8749,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8750,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4057,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8751,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8752,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8753,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4058,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8754,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8755,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4059,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8756,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 8757,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4060,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8758,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8759,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8760,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4061,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8761,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8762,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4062,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8763,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8764,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4063,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8765,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8766,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 8767,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4064,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8768,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8769,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8770,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4065,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8771,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8772,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Calota DE",
        #         "estaOk": True,
        #         "codigoModelo": 4066,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8773,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4067,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8774,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8775,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8776,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4068,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8777,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8778,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8779,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4069,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8780,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8781,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8791,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4073,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8792,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8782,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4070,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8783,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8784,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8785,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4071,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8786,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8787,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8788,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4072,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8789,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8790,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Coluna Esq",
        #         "estaOk": True,
        #         "codigoModelo": 4074,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Adesivado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8793,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4075,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8794,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8795,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8796,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4076,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8797,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8798,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8799,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4077,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8800,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8801,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8802,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4078,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8803,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8804,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4079,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8805,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 8806,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4080,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8807,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8808,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8809,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4081,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8810,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8811,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4082,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8812,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8813,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4083,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8814,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8815,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 8816,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4084,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8817,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8818,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8819,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4085,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8820,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8821,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Entrada de Porta DE",
        #         "estaOk": True,
        #         "codigoModelo": 4086,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8822,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4087,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8823,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8824,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8825,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4088,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8826,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8827,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8828,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4089,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8829,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8830,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4090,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8831,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 8832,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4091,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8833,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8834,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8835,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4092,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8836,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8837,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4093,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8838,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8839,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4094,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8840,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8841,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 8842,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4095,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8843,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8844,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8845,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4096,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8846,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8847,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Forro de Porta DE",
        #         "estaOk": True,
        #         "codigoModelo": 4097,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8848,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4098,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8849,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8850,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8851,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4099,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8852,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8853,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desfiado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8854,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4100,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8855,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8856,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8857,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4101,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8858,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8859,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4102,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8860,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8861,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8862,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4103,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8863,
        #                 "descricao": "Limpar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8864,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8865,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4104,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8866,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8867,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4105,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8868,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8869,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 8870,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4106,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8871,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8872,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Friso/Borrachão Esq",
        #         "estaOk": True,
        #         "codigoModelo": 4107,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Avariado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8873,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4108,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8874,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8875,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desalinhado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8876,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4109,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8877,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8878,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8879,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4110,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8880,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8881,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4111,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8882,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 8883,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4112,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8884,
        #                 "descricao": "Fixar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8885,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Guarnição DE",
        #         "estaOk": True,
        #         "codigoModelo": 4113,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8886,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4114,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8887,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8888,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4115,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8889,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8890,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8891,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4116,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8892,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8893,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4117,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8894,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8895,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4118,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8896,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8897,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8898,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4119,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8899,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 8900,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4120,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8901,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8902,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Insulfilm DE",
        #         "estaOk": True,
        #         "codigoModelo": 4121,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Avariado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8903,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4122,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8904,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8905,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8906,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4123,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8907,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Maçaneta DE",
        #         "estaOk": True,
        #         "codigoModelo": 4124,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8908,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4125,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8909,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8910,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4126,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8911,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Abre",
        #             "valorProblema": "",
        #             "codigoPergunta": 8912,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4127,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8913,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8914,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8915,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4128,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8916,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8917,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4129,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8918,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8919,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8920,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4130,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8921,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8922,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 8923,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4131,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8924,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8925,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8926,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4132,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8927,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8928,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Para Barro Esq",
        #         "estaOk": True,
        #         "codigoModelo": 4134,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8930,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4135,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8931,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8932,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8933,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4136,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8934,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8935,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8936,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4137,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8937,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8938,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4138,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8939,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8940,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8941,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4139,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8942,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8943,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4140,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8944,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8945,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Para Lama Esq",
        #         "estaOk": True,
        #         "codigoModelo": 4141,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Adesivado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8946,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4142,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8947,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8948,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8949,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4143,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8950,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8951,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8952,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4144,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8953,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8954,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8955,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4145,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8956,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8957,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4146,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8958,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 8959,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4147,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8960,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8961,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8962,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4148,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8963,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8964,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4149,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8965,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8966,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4150,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8967,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8968,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 8969,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4151,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8970,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8971,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 8972,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4152,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8973,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8974,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Porta DE",
        #         "estaOk": None,
        #         "codigoModelo": 4153,
        #         "item": {
        #             "obrigatorio": True,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Adesivado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8975,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4154,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8976,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8977,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8978,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4155,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8979,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8980,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8981,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4156,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8982,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8983,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8984,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4157,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8985,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8986,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4158,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8987,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 8988,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4159,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8989,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8990,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8991,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4160,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8992,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8993,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4161,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8994,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 8995,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4162,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8996,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8997,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 8998,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4163,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8999,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9000,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 9001,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4164,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9002,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9003,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Retrovisor DE",
        #         "estaOk": True,
        #         "codigoModelo": 4165,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9004,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4166,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9005,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9006,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4167,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9007,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Abre",
        #             "valorProblema": "",
        #             "codigoPergunta": 9008,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4168,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9009,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9010,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9011,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4169,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9012,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 9013,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4170,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9014,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9015,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9016,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4171,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9017,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9018,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 9019,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4172,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9020,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9021,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 9022,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4173,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9023,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9024,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Roda DE",
        #         "estaOk": True,
        #         "codigoModelo": 4174,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [{
        #                 "codigo": 4175,
        #                 "descricao": "Modelo",
        #                 "obrigatorio": False,
        #                 "visivel": True,
        #                 "ordem": 0,
        #                 "listaResposta": [{
        #                     "descricao": "Ferro",
        #                     "valor": "",
        #                     "codigoPergunta": 9025,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Liga Leve",
        #                     "valor": "",
        #                     "codigoPergunta": 9026,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }]
        #             }],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9027,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4183,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9043,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 13297,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9030,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4176,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9028,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9029,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9032,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4177,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9031,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9034,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4178,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9033,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9036,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4179,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9035,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 9038,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4180,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9037,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 9040,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4181,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9039,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 9042,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4182,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9041,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Vidro porta DE",
        #         "estaOk": True,
        #         "codigoModelo": 4184,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9044,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4185,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9045,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 9046,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4186,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9047,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9048,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9049,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4187,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9050,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9051,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 9052,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4188,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9053,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9054,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Vidro Retrovisor DE",
        #         "estaOk": True,
        #         "codigoModelo": 4189,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9055,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4190,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9056,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9057,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4191,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9058,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9059,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4192,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9060,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9061,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4193,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9062,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 9063,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4194,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9064,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9065,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Outros",
        #         "estaOk": True,
        #         "codigoModelo": 4133,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 2,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8929,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 5372,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 13296,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }]
        #     }],
        #     "ehParteDesenho": True,
        #     "codigoParte": 4037
        # }, {
        #     "parte": "Interior",
        #     "habilitadoEdicao": True,
        #     "listaItemResposta": [{
        #         "descricaoItem": "Alto Falante DD",
        #         "estaOk": True,
        #         "codigoModelo": 3880,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Chiando/Estourado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8350,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3881,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8351,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8352,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8353,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3882,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8354,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Funciona",
        #             "valorProblema": "",
        #             "codigoPergunta": 8355,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3883,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8356,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8357,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8358,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3884,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8359,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Alto Falante DE",
        #         "estaOk": True,
        #         "codigoModelo": 4038,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Chiando/Estourado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8708,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4039,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8709,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8710,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 8711,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4040,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8712,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Funciona",
        #             "valorProblema": "",
        #             "codigoPergunta": 8713,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4041,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8714,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8715,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8716,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4042,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8717,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Alto Falante TD",
        #         "estaOk": True,
        #         "codigoModelo": 4715,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Chiando/Estourado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10267,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4716,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10268,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10269,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 10270,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4717,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10271,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Funciona",
        #             "valorProblema": "",
        #             "codigoPergunta": 10272,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4718,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10273,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10274,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10275,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4719,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10276,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Alto Falante TE",
        #         "estaOk": True,
        #         "codigoModelo": 4835,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Chiando/Estourado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10538,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4836,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10539,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10540,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 10541,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4837,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10542,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Funciona",
        #             "valorProblema": "",
        #             "codigoPergunta": 10543,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4838,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10544,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10545,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10546,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4839,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10547,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Ar Condicionado",
        #         "estaOk": None,
        #         "codigoModelo": 4203,
        #         "item": {
        #             "obrigatorio": True,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Barulho anormal",
        #             "valorProblema": "",
        #             "codigoPergunta": 9081,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4204,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9082,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9083,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9084,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4205,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9085,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Iluminação Queimada",
        #             "valorProblema": "",
        #             "codigoPergunta": 9086,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4206,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9087,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9088,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "infiltrando Agua",
        #             "valorProblema": "",
        #             "codigoPergunta": 9089,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4207,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9090,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9091,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mau Cheiro",
        #             "valorProblema": "",
        #             "codigoPergunta": 9092,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4208,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9093,
        #                 "descricao": "Higienizar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9094,
        #                 "descricao": "Substituir Filtro",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Funciona",
        #             "valorProblema": "",
        #             "codigoPergunta": 9095,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4209,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9096,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9097,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não gela/Fraco",
        #             "valorProblema": "",
        #             "codigoPergunta": 9098,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4210,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9099,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9100,
        #                 "descricao": "Repor Gas",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9101,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9102,
        #                 "descricao": "Substituir Filtro",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9103,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4211,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9104,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9105,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4212,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9106,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9107,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Assoalho Cabine",
        #         "estaOk": True,
        #         "codigoModelo": 4213,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9108,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4214,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9109,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9110,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9111,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4215,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9112,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9113,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9114,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4216,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9115,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9116,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4217,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9117,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 9118,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4218,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9119,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9120,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9121,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4219,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9122,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9123,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4220,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9124,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 9125,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4221,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9126,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9127,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 9128,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4222,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9129,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9130,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 9131,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4223,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9132,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9133,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Banco DD",
        #         "estaOk": True,
        #         "codigoModelo": 4232,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9153,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4233,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9154,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9155,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9156,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4234,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9157,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9158,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desfiado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9159,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4235,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9160,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9161,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9162,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4236,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9163,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9164,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4237,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9165,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9166,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9167,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4238,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9168,
        #                 "descricao": "Limpar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9169,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9170,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4239,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9171,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9172,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4240,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9173,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9174,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 9175,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4241,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9176,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9177,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Banco DE",
        #         "estaOk": True,
        #         "codigoModelo": 4242,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9178,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4243,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9179,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9180,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9181,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4244,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9182,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9183,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desfiado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9184,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4245,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9185,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9186,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9187,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4246,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9188,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9189,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4247,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9190,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9191,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9192,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4248,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9193,
        #                 "descricao": "Limpar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9194,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9195,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4249,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9196,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9197,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4250,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9198,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9199,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 9200,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4251,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9201,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9202,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Banco TRAS",
        #         "estaOk": True,
        #         "codigoModelo": 4252,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9203,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4253,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9204,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9205,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9206,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4254,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9207,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9208,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desfiado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9209,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4255,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9210,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9211,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9212,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4256,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9213,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9214,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4257,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9215,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9216,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9217,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4258,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9218,
        #                 "descricao": "Limpar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9219,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9220,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4259,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9221,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9222,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4260,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9223,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9224,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 9225,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4261,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9226,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9227,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Buzina",
        #         "estaOk": True,
        #         "codigoModelo": 4262,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9228,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4263,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9229,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9230,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desacascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9231,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4264,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9232,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9233,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9234,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4265,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9235,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9236,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Funciona",
        #             "valorProblema": "",
        #             "codigoPergunta": 9237,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4266,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9238,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9239,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9240,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4267,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9241,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9242,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4268,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9243,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9244,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Carpete Cabine",
        #         "estaOk": True,
        #         "codigoModelo": 4269,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9245,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4270,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9246,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desgastado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9247,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4271,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9248,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9249,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4272,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9250,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9251,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4273,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9252,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9253,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4274,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9254,
        #                 "descricao": "Limpar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9255,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9256,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4275,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9257,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Rasgado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9258,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4276,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9259,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Cinto de Seg DD",
        #         "estaOk": True,
        #         "codigoModelo": 4277,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9260,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4278,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9261,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9262,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9263,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4279,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9264,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9265,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desfiado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9266,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4280,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9267,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9268,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9269,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4281,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9270,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9271,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4282,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9272,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9273,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9274,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4283,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9275,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9276,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Retorna",
        #             "valorProblema": "",
        #             "codigoPergunta": 9277,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4284,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9278,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9279,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não trava",
        #             "valorProblema": "",
        #             "codigoPergunta": 9280,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4285,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9281,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9282,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9283,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4286,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9284,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 9285,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4287,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9286,
        #                 "descricao": "Fixar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Cinto de Seg DE",
        #         "estaOk": True,
        #         "codigoModelo": 4288,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9287,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4289,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9288,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9289,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9290,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4290,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9291,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9292,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desfiado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9293,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4291,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9294,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9295,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9296,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4292,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9297,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9298,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4293,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9299,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9300,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9301,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4294,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9302,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9303,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Retorna",
        #             "valorProblema": "",
        #             "codigoPergunta": 9304,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4295,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9305,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9306,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não trava",
        #             "valorProblema": "",
        #             "codigoPergunta": 9307,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4296,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9308,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9309,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9310,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4297,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9311,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 9312,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4298,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9313,
        #                 "descricao": "Fixar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Cinto de Seg TRAS",
        #         "estaOk": True,
        #         "codigoModelo": 4299,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9314,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4300,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9315,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9316,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9317,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4301,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9318,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9319,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desfiado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9320,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4302,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9321,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9322,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9323,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4303,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9324,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9325,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4304,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9326,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9327,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9328,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4305,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9329,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9330,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Retorna",
        #             "valorProblema": "",
        #             "codigoPergunta": 9331,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4306,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9332,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9333,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não trava",
        #             "valorProblema": "",
        #             "codigoPergunta": 9334,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4307,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9335,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9336,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9337,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4308,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9338,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 9339,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4309,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9340,
        #                 "descricao": "Fixar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Coifa da Alavanca",
        #         "estaOk": True,
        #         "codigoModelo": 4316,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9353,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4317,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9354,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9355,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4318,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9356,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9357,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4319,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9358,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9359,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4320,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9360,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9361,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9362,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4321,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9363,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9364,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4322,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9365,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9366,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 9367,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4323,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9368,
        #                 "descricao": "Fixar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9369,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9370,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Console Interno",
        #         "estaOk": True,
        #         "codigoModelo": 4324,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9371,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4325,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9372,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9373,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desacascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9374,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4326,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9375,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9376,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9377,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4327,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9378,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9379,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4328,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9380,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9381,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9382,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4329,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9383,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9384,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9385,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4330,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9386,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9387,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4331,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9388,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9389,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 9390,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4332,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9391,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9392,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Difusor Ar Central",
        #         "estaOk": True,
        #         "codigoModelo": 4338,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9402,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4339,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9403,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não sai Ar",
        #             "valorProblema": "",
        #             "codigoPergunta": 9404,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4340,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9405,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9406,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9407,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4341,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9408,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9409,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4342,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9410,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9411,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 9412,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4343,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9413,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9414,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Travado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9415,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4344,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9416,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9417,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Difusor de Ar Dir",
        #         "estaOk": True,
        #         "codigoModelo": 4345,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9418,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4346,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9419,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não sai Ar",
        #             "valorProblema": "",
        #             "codigoPergunta": 9420,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4347,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9421,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9422,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9423,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4348,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9424,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9425,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4349,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9426,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9427,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 9428,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4350,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9429,
        #                 "descricao": "Fixar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9430,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Travado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9431,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4351,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9432,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9433,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Difusor de Ar Esq",
        #         "estaOk": True,
        #         "codigoModelo": 4352,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9434,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4353,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9435,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não sai Ar",
        #             "valorProblema": "",
        #             "codigoPergunta": 9436,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4354,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9437,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9438,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9439,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4355,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9440,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9441,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4356,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9442,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9443,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 9444,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4357,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9445,
        #                 "descricao": "Fixar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9446,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Travado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9447,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4358,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9448,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9449,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Forro de Teto",
        #         "estaOk": True,
        #         "codigoModelo": 4359,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9450,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4360,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9451,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9452,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Cortado/Riscado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9453,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4361,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9454,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9455,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desfiado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9456,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4362,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9457,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9458,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9459,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4363,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9460,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9461,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4364,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9462,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9463,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9464,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4365,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9465,
        #                 "descricao": "Limpar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9466,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9467,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9468,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4366,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9469,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 9470,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4367,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9471,
        #                 "descricao": "Fixar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Forro tampa Tras",
        #         "estaOk": True,
        #         "codigoModelo": 4637,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10102,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4638,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10103,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 10104,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4639,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10105,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10106,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Limp/Comando seta",
        #         "estaOk": True,
        #         "codigoModelo": 4368,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Não Funciona",
        #             "valorProblema": "",
        #             "codigoPergunta": 9472,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4369,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9473,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9474,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Retorna",
        #             "valorProblema": "",
        #             "codigoPergunta": 9475,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4370,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9476,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9477,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9478,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4371,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9479,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9480,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4372,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9481,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9482,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Moldura Radio",
        #         "estaOk": True,
        #         "codigoModelo": 4373,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9483,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4374,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9484,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9485,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9486,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4375,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9487,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9488,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9489,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4376,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9490,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9491,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4377,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9492,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9493,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9494,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4378,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9495,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9496,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9497,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4379,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9498,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9499,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4380,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9500,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9501,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 9502,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4381,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9503,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9504,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Painel inst/Tabelier",
        #         "estaOk": True,
        #         "codigoModelo": 4383,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9506,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4384,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9507,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9508,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Cortado/Riscado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9509,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4385,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9510,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9511,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9512,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4386,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9513,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9514,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9515,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4387,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9516,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9517,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4388,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9518,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9519,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Iluminação Queimada",
        #             "valorProblema": "",
        #             "codigoPergunta": 9520,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4389,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9521,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9522,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9523,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4390,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9524,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9525,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mau Contato",
        #             "valorProblema": "",
        #             "codigoPergunta": 9526,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4391,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9527,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9528,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Funciona",
        #             "valorProblema": "",
        #             "codigoPergunta": 9529,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4392,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9530,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9531,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9532,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4393,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9533,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9534,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4394,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9535,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9536,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solta/Barulho",
        #             "valorProblema": "",
        #             "codigoPergunta": 9537,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4395,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9538,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Quebra Sol DIR",
        #         "estaOk": True,
        #         "codigoModelo": 4396,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado/Riscado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9539,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4397,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9540,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9541,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9542,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4398,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9543,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9544,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4399,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9545,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9546,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9547,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4400,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9548,
        #                 "descricao": "Limpar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9549,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9550,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4401,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9551,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9552,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4402,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9553,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9554,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 9555,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4403,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9556,
        #                 "descricao": "Fixar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Quebra Sol ESQ",
        #         "estaOk": True,
        #         "codigoModelo": 4404,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado/Riscado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9557,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4405,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9558,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9559,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9560,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4406,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9561,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9562,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4407,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9563,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9564,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9565,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4408,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9566,
        #                 "descricao": "Limpar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9567,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9568,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4409,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9569,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9570,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4410,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9571,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9572,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 9573,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4411,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9574,
        #                 "descricao": "Fixar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Retrovisor",
        #         "estaOk": True,
        #         "codigoModelo": 4412,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9575,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4413,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9576,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Abre",
        #             "valorProblema": "",
        #             "codigoPergunta": 9577,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4414,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9578,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9579,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9580,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4415,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9581,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9582,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4416,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9583,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9584,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Som/Frente",
        #         "estaOk": True,
        #         "codigoModelo": 4417,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Display Apagado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9585,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4418,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9586,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9587,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9588,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4419,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9589,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Funciona",
        #             "valorProblema": "",
        #             "codigoPergunta": 9590,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4420,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9591,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9592,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Sintoniza",
        #             "valorProblema": "",
        #             "codigoPergunta": 9593,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4421,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9594,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9595,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9596,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4422,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9597,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9598,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4423,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9599,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9600,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Tapete Borracha",
        #         "estaOk": True,
        #         "codigoModelo": 4442,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9645,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4443,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9646,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desgastado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9647,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4444,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9648,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9649,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4445,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9650,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9651,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4446,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9652,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9653,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4447,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9654,
        #                 "descricao": "Limpar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9655,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9656,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4448,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9657,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Rasgado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9658,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4449,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9659,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Volante",
        #         "estaOk": True,
        #         "codigoModelo": 4458,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Avariado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9675,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4459,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9676,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9677,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9678,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4460,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9679,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9680,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desalinhado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9684,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4462,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9685,
        #                 "descricao": "Alinhar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9681,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4461,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9682,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9683,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9686,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4463,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9687,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9688,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4464,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9689,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9690,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9691,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4465,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9692,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9693,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4466,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9694,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9695,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Trepidando",
        #             "valorProblema": "",
        #             "codigoPergunta": 9696,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4467,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9697,
        #                 "descricao": "Balancear",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Outros",
        #         "estaOk": True,
        #         "codigoModelo": 4382,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 2,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9505,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 5373,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 13301,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }]
        #     }],
        #     "ehParteDesenho": True,
        #     "codigoParte": 4195
        # }, {
        #     "parte": "Partes Moveis",
        #     "habilitadoEdicao": True,
        #     "listaItemResposta": [{
        #         "descricaoItem": "Adesivo",
        #         "estaOk": True,
        #         "codigoModelo": 6686,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Possui adesivo",
        #             "valorProblema": "",
        #             "codigoPergunta": 16334,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6687,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16335,
        #                 "descricao": "Retirar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Cartão Code",
        #         "estaOk": True,
        #         "codigoModelo": 4469,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9698,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4470,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9699,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9700,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4471,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9701,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9702,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4472,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9703,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Rasgado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9704,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4473,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9705,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Chave de Roda",
        #         "estaOk": True,
        #         "codigoModelo": 4474,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9706,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4475,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9707,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9708,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4476,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9709,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9710,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4477,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9711,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9712,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9713,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4478,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9714,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9715,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Chave Principal",
        #         "estaOk": True,
        #         "codigoModelo": 4479,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Desgaste Irregular",
        #             "valorProblema": "",
        #             "codigoPergunta": 9716,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4480,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9717,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9718,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9719,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4481,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9720,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Funciona",
        #             "valorProblema": "",
        #             "codigoPergunta": 9721,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4482,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9722,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9723,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9724,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4483,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9725,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9726,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4484,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9727,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9728,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Rasgaddo",
        #             "valorProblema": "",
        #             "codigoPergunta": 9729,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4485,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9730,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9731,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Controle do Alarme",
        #         "estaOk": True,
        #         "codigoModelo": 4493,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Desgaste Irregular",
        #             "valorProblema": "",
        #             "codigoPergunta": 9748,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4494,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9749,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9750,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9751,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4495,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9752,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Funciona",
        #             "valorProblema": "",
        #             "codigoPergunta": 9753,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4496,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9754,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9755,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9756,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4497,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9757,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9758,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4498,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9759,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9760,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Rasgaddo",
        #             "valorProblema": "",
        #             "codigoPergunta": 9761,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4499,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9762,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9763,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Documento CRLV",
        #         "estaOk": None,
        #         "codigoModelo": 4500,
        #         "item": {
        #             "obrigatorio": True,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9764,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4501,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9765,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9766,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4502,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9767,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Rasgado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9768,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4503,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9769,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Rasurado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9770,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4504,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9771,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Macaco",
        #         "estaOk": True,
        #         "codigoModelo": 4509,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9778,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4510,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9779,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não funciona",
        #             "valorProblema": "",
        #             "codigoPergunta": 9780,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4511,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9781,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9782,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9783,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4512,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9784,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9785,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4513,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9786,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9787,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9788,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4514,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9789,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9790,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Manual de Garantia",
        #         "estaOk": True,
        #         "codigoModelo": 4515,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9791,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4516,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9792,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9793,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4517,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9794,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Rasgado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9795,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4518,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9796,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Rasurado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9797,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4519,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9798,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Manual Manutenção",
        #         "estaOk": True,
        #         "codigoModelo": 4520,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9799,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4521,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9800,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9801,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4522,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9802,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Rasgado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9803,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4523,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9804,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Rasurado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9805,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4524,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9806,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Observações Gerais",
        #         "estaOk": True,
        #         "codigoModelo": 4525,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9807,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4526,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9808,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Tapetes",
        #         "estaOk": True,
        #         "codigoModelo": 6675,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 16317,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6676,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16318,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 16319,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6677,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16320,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Rasgado",
        #             "valorProblema": "",
        #             "codigoPergunta": 16321,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6678,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16322,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Triângulo",
        #         "estaOk": True,
        #         "codigoModelo": 4527,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9809,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4528,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9810,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9811,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4529,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9812,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9813,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4530,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9814,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9815,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }],
        #     "ehParteDesenho": True,
        #     "codigoParte": 4468
        # }, {
        #     "parte": "Pneu",
        #     "habilitadoEdicao": True,
        #     "listaItemResposta": [{
        #         "descricaoItem": "Estepe",
        #         "estaOk": True,
        #         "codigoModelo": 4532,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [{
        #                 "codigo": 4533,
        #                 "descricao": "Marca",
        #                 "obrigatorio": False,
        #                 "visivel": True,
        #                 "ordem": 0,
        #                 "listaResposta": [{
        #                     "descricao": "Bridgestone",
        #                     "valor": "",
        #                     "codigoPergunta": 16346,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Continental",
        #                     "valor": "",
        #                     "codigoPergunta": 9816,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Firestone",
        #                     "valor": "",
        #                     "codigoPergunta": 9817,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Goodyear",
        #                     "valor": "",
        #                     "codigoPergunta": 9818,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Michelin",
        #                     "valor": "",
        #                     "codigoPergunta": 9819,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Outros",
        #                     "valor": "",
        #                     "codigoPergunta": 9821,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Pireli",
        #                     "valor": "",
        #                     "codigoPergunta": 9820,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }]
        #             }, {
        #                 "codigo": 4534,
        #                 "descricao": "Medida",
        #                 "obrigatorio": True,
        #                 "visivel": True,
        #                 "ordem": 0,
        #                 "listaResposta": [{
        #                     "descricao": "175/65 R 14",
        #                     "valor": "",
        #                     "codigoPergunta": 9822,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "175/70 R14",
        #                     "valor": "",
        #                     "codigoPergunta": 9823,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/60 R 14",
        #                     "valor": "",
        #                     "codigoPergunta": 9824,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/60 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9825,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/65 R 14",
        #                     "valor": "",
        #                     "codigoPergunta": 9826,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/65 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9827,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/70 R 14",
        #                     "valor": "",
        #                     "codigoPergunta": 9828,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/80 R 14",
        #                     "valor": "",
        #                     "codigoPergunta": 9829,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "195/55 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9830,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "195/55 R 16",
        #                     "valor": "",
        #                     "codigoPergunta": 9831,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "195/60 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9832,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "195/65 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9833,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "205/55 R 16",
        #                     "valor": "",
        #                     "codigoPergunta": 9834,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "205/70 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9835,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Outros",
        #                     "valor": "",
        #                     "codigoPergunta": 9836,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }]
        #             }, {
        #                 "codigo": 4535,
        #                 "descricao": "TWI",
        #                 "obrigatorio": True,
        #                 "visivel": True,
        #                 "ordem": 0,
        #                 "listaResposta": [{
        #                     "descricao": "",
        #                     "valor": "",
        #                     "codigoPergunta": 9837,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }]
        #             }],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Abaixo TWI",
        #             "valorProblema": "",
        #             "codigoPergunta": 9838,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4538,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9843,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Avariado/Bolha",
        #             "valorProblema": "",
        #             "codigoPergunta": 9840,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 0,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": []
        #         }, {
        #             "descricaoProblema": "Desgaste Irregular",
        #             "valorProblema": "",
        #             "codigoPergunta": 9842,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 0,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": []
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9844,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4536,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9839,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Marca",
        #             "valorProblema": "",
        #             "codigoPergunta": 13302,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 5374,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 13303,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 13304,
        #                 "descricao": "Rodizio",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9846,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4537,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9841,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Pneu DD",
        #         "estaOk": True,
        #         "codigoModelo": 4542,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [{
        #                 "codigo": 4543,
        #                 "descricao": "Marca",
        #                 "obrigatorio": False,
        #                 "visivel": True,
        #                 "ordem": 0,
        #                 "listaResposta": [{
        #                     "descricao": "BRIDGESTONE",
        #                     "valor": "",
        #                     "codigoPergunta": 16345,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Continental",
        #                     "valor": "",
        #                     "codigoPergunta": 9849,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Firestone",
        #                     "valor": "True",
        #                     "codigoPergunta": 9850,
        #                     "resposta": True,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Goodyear",
        #                     "valor": "",
        #                     "codigoPergunta": 9851,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Michelin",
        #                     "valor": "",
        #                     "codigoPergunta": 9852,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Outros",
        #                     "valor": "",
        #                     "codigoPergunta": 9854,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Pireli",
        #                     "valor": "",
        #                     "codigoPergunta": 9853,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }]
        #             }, {
        #                 "codigo": 4544,
        #                 "descricao": "Medida",
        #                 "obrigatorio": False,
        #                 "visivel": True,
        #                 "ordem": 0,
        #                 "listaResposta": [{
        #                     "descricao": "175/65 R 14",
        #                     "valor": "",
        #                     "codigoPergunta": 9855,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "175/70 R 14",
        #                     "valor": "",
        #                     "codigoPergunta": 9856,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/60 R 14",
        #                     "valor": "",
        #                     "codigoPergunta": 9857,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/60 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9858,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/65 R 14",
        #                     "valor": "",
        #                     "codigoPergunta": 9859,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/65 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9860,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/70 R 14",
        #                     "valor": "True",
        #                     "codigoPergunta": 9861,
        #                     "resposta": True,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/80 R 14",
        #                     "valor": "",
        #                     "codigoPergunta": 9862,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "195/55 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9863,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "195/55 R 16",
        #                     "valor": "",
        #                     "codigoPergunta": 9864,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "195/60 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9865,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "195/65 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9866,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "205/55 R 16",
        #                     "valor": "",
        #                     "codigoPergunta": 9867,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "205/70 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9868,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Outros",
        #                     "valor": "",
        #                     "codigoPergunta": 9869,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }]
        #             }, {
        #                 "codigo": 4545,
        #                 "descricao": "TWI",
        #                 "obrigatorio": False,
        #                 "visivel": True,
        #                 "ordem": 0,
        #                 "listaResposta": [{
        #                     "descricao": "",
        #                     "valor": "",
        #                     "codigoPergunta": 9870,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }]
        #             }],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Abaixo TWI",
        #             "valorProblema": "",
        #             "codigoPergunta": 9871,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4548,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9876,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Avariado/Bolha",
        #             "valorProblema": "",
        #             "codigoPergunta": 9873,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 0,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": []
        #         }, {
        #             "descricaoProblema": "Desgaste Irregular",
        #             "valorProblema": "",
        #             "codigoPergunta": 9875,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 0,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": []
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "True",
        #             "codigoPergunta": 9877,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4546,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9872,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Marca",
        #             "valorProblema": "",
        #             "codigoPergunta": 13305,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 5375,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 13306,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 13307,
        #                 "descricao": "Rodizio",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9879,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4547,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9874,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Pneu DE",
        #         "estaOk": None,
        #         "codigoModelo": 4551,
        #         "item": {
        #             "obrigatorio": True,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [{
        #                 "codigo": 4552,
        #                 "descricao": "Marca",
        #                 "obrigatorio": False,
        #                 "visivel": True,
        #                 "ordem": 0,
        #                 "listaResposta": [{
        #                     "descricao": "Bridgestone",
        #                     "valor": "",
        #                     "codigoPergunta": 16347,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Continental",
        #                     "valor": "",
        #                     "codigoPergunta": 9881,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Firestone",
        #                     "valor": "True",
        #                     "codigoPergunta": 9882,
        #                     "resposta": True,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Goodyear",
        #                     "valor": "",
        #                     "codigoPergunta": 9883,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Michelin",
        #                     "valor": "",
        #                     "codigoPergunta": 9884,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Outros",
        #                     "valor": "",
        #                     "codigoPergunta": 9886,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Pireli",
        #                     "valor": "",
        #                     "codigoPergunta": 9885,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }]
        #             }, {
        #                 "codigo": 4553,
        #                 "descricao": "Medida",
        #                 "obrigatorio": False,
        #                 "visivel": True,
        #                 "ordem": 0,
        #                 "listaResposta": [{
        #                     "descricao": "175/65 R 14",
        #                     "valor": "",
        #                     "codigoPergunta": 9887,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "175/70 R 14",
        #                     "valor": "",
        #                     "codigoPergunta": 9888,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/60 R 14",
        #                     "valor": "",
        #                     "codigoPergunta": 9889,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/60 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9890,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/65 R 14",
        #                     "valor": "",
        #                     "codigoPergunta": 9891,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/65 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9892,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/70 R 14",
        #                     "valor": "True",
        #                     "codigoPergunta": 9893,
        #                     "resposta": True,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/80 R 14",
        #                     "valor": "",
        #                     "codigoPergunta": 9894,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "195/55 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9895,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "195/55 R 16",
        #                     "valor": "",
        #                     "codigoPergunta": 9896,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "195/60 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9897,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "195/65 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9898,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "205/55 R 16",
        #                     "valor": "",
        #                     "codigoPergunta": 9899,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "205/70 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9900,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Outros",
        #                     "valor": "",
        #                     "codigoPergunta": 9901,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }]
        #             }, {
        #                 "codigo": 4554,
        #                 "descricao": "TWI",
        #                 "obrigatorio": False,
        #                 "visivel": True,
        #                 "ordem": 0,
        #                 "listaResposta": [{
        #                     "descricao": "",
        #                     "valor": "",
        #                     "codigoPergunta": 9902,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }]
        #             }],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Abaixo TWI",
        #             "valorProblema": "",
        #             "codigoPergunta": 9903,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4557,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9908,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Avariado/Bolha",
        #             "valorProblema": "",
        #             "codigoPergunta": 9905,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 0,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": []
        #         }, {
        #             "descricaoProblema": "Desgaste Irregular",
        #             "valorProblema": "",
        #             "codigoPergunta": 9907,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 0,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": []
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "True",
        #             "codigoPergunta": 9909,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4555,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9904,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Marca",
        #             "valorProblema": "",
        #             "codigoPergunta": 13308,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 5376,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 13309,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 13310,
        #                 "descricao": "Rodizio",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9911,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4556,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9906,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Pneu TD",
        #         "estaOk": True,
        #         "codigoModelo": 4560,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [{
        #                 "codigo": 4561,
        #                 "descricao": "Marca",
        #                 "obrigatorio": False,
        #                 "visivel": True,
        #                 "ordem": 0,
        #                 "listaResposta": [{
        #                     "descricao": "Bridgestone",
        #                     "valor": "",
        #                     "codigoPergunta": 16348,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Continental",
        #                     "valor": "",
        #                     "codigoPergunta": 9913,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Firestone",
        #                     "valor": "True",
        #                     "codigoPergunta": 9914,
        #                     "resposta": True,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Goodyear",
        #                     "valor": "",
        #                     "codigoPergunta": 9915,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Michelin",
        #                     "valor": "",
        #                     "codigoPergunta": 9916,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Outros",
        #                     "valor": "",
        #                     "codigoPergunta": 9918,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Pireli",
        #                     "valor": "",
        #                     "codigoPergunta": 9917,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }]
        #             }, {
        #                 "codigo": 4562,
        #                 "descricao": "Medida",
        #                 "obrigatorio": False,
        #                 "visivel": True,
        #                 "ordem": 0,
        #                 "listaResposta": [{
        #                     "descricao": "175/65 R 14",
        #                     "valor": "",
        #                     "codigoPergunta": 9919,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "175/70 R14",
        #                     "valor": "",
        #                     "codigoPergunta": 9920,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/60 R 14",
        #                     "valor": "",
        #                     "codigoPergunta": 9921,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/60 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9922,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/65 R 14",
        #                     "valor": "",
        #                     "codigoPergunta": 9923,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/65 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9924,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/70 R 14",
        #                     "valor": "True",
        #                     "codigoPergunta": 9925,
        #                     "resposta": True,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/80 R 14",
        #                     "valor": "",
        #                     "codigoPergunta": 9926,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "195/55 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9927,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "195/55 R 16",
        #                     "valor": "",
        #                     "codigoPergunta": 9928,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "195/60 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9929,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "195/65 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9930,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "205/55 R 16",
        #                     "valor": "",
        #                     "codigoPergunta": 9931,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "205/70 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9932,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Outros",
        #                     "valor": "",
        #                     "codigoPergunta": 9933,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }]
        #             }, {
        #                 "codigo": 4563,
        #                 "descricao": "TWI",
        #                 "obrigatorio": False,
        #                 "visivel": True,
        #                 "ordem": 0,
        #                 "listaResposta": [{
        #                     "descricao": "",
        #                     "valor": "",
        #                     "codigoPergunta": 9934,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }]
        #             }],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Abaixo TWI",
        #             "valorProblema": "",
        #             "codigoPergunta": 9935,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4566,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9940,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Avariado/Bolha",
        #             "valorProblema": "",
        #             "codigoPergunta": 9937,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 0,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": []
        #         }, {
        #             "descricaoProblema": "Desgaste Irregular",
        #             "valorProblema": "",
        #             "codigoPergunta": 9939,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 0,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": []
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "True",
        #             "codigoPergunta": 9941,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4564,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9936,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Marca",
        #             "valorProblema": "",
        #             "codigoPergunta": 13311,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 5377,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 13312,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 13313,
        #                 "descricao": "Rodizio",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9943,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4565,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9938,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Pneu TE",
        #         "estaOk": True,
        #         "codigoModelo": 4569,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [{
        #                 "codigo": 4570,
        #                 "descricao": "Marca",
        #                 "obrigatorio": False,
        #                 "visivel": True,
        #                 "ordem": 0,
        #                 "listaResposta": [{
        #                     "descricao": "Bridgestone",
        #                     "valor": "",
        #                     "codigoPergunta": 16349,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Continental",
        #                     "valor": "",
        #                     "codigoPergunta": 9945,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Firestone",
        #                     "valor": "True",
        #                     "codigoPergunta": 9946,
        #                     "resposta": True,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Goodyear",
        #                     "valor": "",
        #                     "codigoPergunta": 9947,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Michelin",
        #                     "valor": "",
        #                     "codigoPergunta": 9948,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Outros",
        #                     "valor": "",
        #                     "codigoPergunta": 9950,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Pireli",
        #                     "valor": "",
        #                     "codigoPergunta": 9949,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }]
        #             }, {
        #                 "codigo": 4571,
        #                 "descricao": "Medida",
        #                 "obrigatorio": False,
        #                 "visivel": True,
        #                 "ordem": 0,
        #                 "listaResposta": [{
        #                     "descricao": "175/65 R 14",
        #                     "valor": "",
        #                     "codigoPergunta": 9951,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "175/70 R14",
        #                     "valor": "",
        #                     "codigoPergunta": 9952,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/60 R 14",
        #                     "valor": "",
        #                     "codigoPergunta": 9953,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/60 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9954,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/65 R 14",
        #                     "valor": "",
        #                     "codigoPergunta": 9955,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/65 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9956,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/70 R 14",
        #                     "valor": "True",
        #                     "codigoPergunta": 9957,
        #                     "resposta": True,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "185/80 R 14",
        #                     "valor": "",
        #                     "codigoPergunta": 9958,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "195/55 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9959,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "195/55 R 16",
        #                     "valor": "",
        #                     "codigoPergunta": 9960,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "195/60 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9961,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "195/65 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9962,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "205/55 R 16",
        #                     "valor": "",
        #                     "codigoPergunta": 9963,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "205/70 R 15",
        #                     "valor": "",
        #                     "codigoPergunta": 9964,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Outros",
        #                     "valor": "",
        #                     "codigoPergunta": 9965,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }]
        #             }, {
        #                 "codigo": 4572,
        #                 "descricao": "TWI",
        #                 "obrigatorio": False,
        #                 "visivel": True,
        #                 "ordem": 0,
        #                 "listaResposta": [{
        #                     "descricao": "",
        #                     "valor": "",
        #                     "codigoPergunta": 9966,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }]
        #             }],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Abaixo TWI",
        #             "valorProblema": "",
        #             "codigoPergunta": 9967,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4575,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9972,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Avariado/Bolha",
        #             "valorProblema": "",
        #             "codigoPergunta": 9969,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 0,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": []
        #         }, {
        #             "descricaoProblema": "Desgaste Irregular",
        #             "valorProblema": "",
        #             "codigoPergunta": 9971,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 0,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": []
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "True",
        #             "codigoPergunta": 9973,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4573,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9968,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Marca",
        #             "valorProblema": "",
        #             "codigoPergunta": 13314,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 5378,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 13315,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 13316,
        #                 "descricao": "Rodizio",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9975,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4574,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9970,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }],
        #     "ehParteDesenho": False,
        #     "codigoParte": 4531
        # }, {
        #     "parte": "Teto",
        #     "habilitadoEdicao": True,
        #     "listaItemResposta": [{
        #         "descricaoItem": "Antena",
        #         "estaOk": True,
        #         "codigoModelo": 4604,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Desacascada",
        #             "valorProblema": "",
        #             "codigoPergunta": 10033,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4605,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10034,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10035,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 10036,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4606,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10037,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10038,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4607,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10039,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10040,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4608,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10041,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10042,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Friso/Borrachão Dir",
        #         "estaOk": True,
        #         "codigoModelo": 4579,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Avariado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9977,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4580,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9978,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9979,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desalinhado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9980,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4581,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9981,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9982,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9983,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4582,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9984,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9985,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4583,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9986,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 9987,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4584,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9988,
        #                 "descricao": "Fixar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9989,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Friso/Borrachão Esq",
        #         "estaOk": True,
        #         "codigoModelo": 4585,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Avariado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9990,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4586,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9991,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9992,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desalinhado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9993,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4587,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9994,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9995,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9996,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4588,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9997,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9998,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4589,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9999,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 10000,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4590,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10001,
        #                 "descricao": "Fixar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10002,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Teto",
        #         "estaOk": None,
        #         "codigoModelo": 4592,
        #         "item": {
        #             "obrigatorio": True,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Adesivado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10004,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4593,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10005,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10006,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10007,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4594,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10008,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10009,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10010,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4595,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10011,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10012,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10013,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4596,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10014,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10015,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4597,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10016,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 10017,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4598,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10018,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10019,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10020,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4599,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10021,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10022,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4600,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10023,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10024,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4601,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10025,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10026,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 10027,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4602,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10028,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10029,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10030,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4603,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10031,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10032,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Outros",
        #         "estaOk": True,
        #         "codigoModelo": 4591,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 2,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10003,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 5379,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 13317,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }]
        #     }],
        #     "ehParteDesenho": True,
        #     "codigoParte": 4578
        # }, {
        #     "parte": "Traseira",
        #     "habilitadoEdicao": True,
        #     "listaItemResposta": [{
        #         "descricaoItem": "Assoalho Mala",
        #         "estaOk": True,
        #         "codigoModelo": 4610,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10043,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4611,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10044,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10045,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4612,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10046,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10047,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4613,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10048,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10049,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4614,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10050,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 10051,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4615,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10052,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10053,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10054,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4616,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10055,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10056,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4617,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10057,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10058,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4618,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10059,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10060,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 10061,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4619,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10062,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10063,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4620,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10064,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Bagagito",
        #         "estaOk": True,
        #         "codigoModelo": 4224,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9134,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4225,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9135,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9136,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desgastado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9137,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4226,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9138,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9139,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9140,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4227,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9141,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9142,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4228,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9143,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9144,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9145,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4229,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9146,
        #                 "descricao": "Limpar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9147,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9148,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4230,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9149,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Rasgado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9150,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4231,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9151,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9152,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Break Light",
        #         "estaOk": True,
        #         "codigoModelo": 4621,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 10065,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4622,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10066,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Infiltração",
        #             "valorProblema": "",
        #             "codigoPergunta": 10067,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4623,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10068,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10069,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Funciona",
        #             "valorProblema": "",
        #             "codigoPergunta": 10070,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4624,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10071,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10072,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10073,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4625,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10074,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10075,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4626,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10076,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10077,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Trincado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10078,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4627,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10079,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10080,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Corda Bagagito",
        #         "estaOk": True,
        #         "codigoModelo": 4333,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9393,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4334,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9394,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desfiando",
        #             "valorProblema": "",
        #             "codigoPergunta": 9395,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4335,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9396,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9397,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9398,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4336,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9399,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9400,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4337,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9401,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Forro Tampa Tras",
        #         "estaOk": True,
        #         "codigoModelo": 4628,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10081,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4629,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10082,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10083,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10084,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4630,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10085,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10086,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desfiado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10087,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4631,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10088,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10089,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 10090,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4632,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10091,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10092,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4633,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10093,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10094,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10095,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4634,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10096,
        #                 "descricao": "Limpar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10097,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10098,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4635,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10099,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10100,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4636,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10101,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Guarnição TRAS",
        #         "estaOk": True,
        #         "codigoModelo": 4640,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10107,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4641,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10108,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10109,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4642,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10110,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10111,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 10112,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4643,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10113,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10114,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4644,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10115,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10116,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4645,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10117,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10118,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10119,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4646,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10120,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 10121,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4647,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10122,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10123,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Insulfilm VidroVigia",
        #         "estaOk": True,
        #         "codigoModelo": 4648,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Avariado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10124,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4649,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10125,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10126,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10127,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4650,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10128,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Limpador/Palheta",
        #         "estaOk": True,
        #         "codigoModelo": 4651,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 10129,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4652,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10130,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10131,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4653,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10132,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10133,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4654,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10134,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10135,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Ressecado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10136,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4655,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10137,
        #                 "descricao": "Substituir ",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Maçaneta Tras",
        #         "estaOk": True,
        #         "codigoModelo": 4656,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10138,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4657,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10139,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 10140,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4658,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10141,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Abre",
        #             "valorProblema": "",
        #             "codigoPergunta": 10142,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4659,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10143,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10144,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10145,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4660,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10146,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10147,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4661,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10148,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10149,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10150,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4662,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10151,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10152,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 10153,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4663,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10154,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10155,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10156,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4664,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10157,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10158,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Painel Tras",
        #         "estaOk": True,
        #         "codigoModelo": 4666,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Adesivado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10160,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4667,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10161,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10162,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10163,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4668,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10164,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10165,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10166,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4669,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10167,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10168,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10169,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4670,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10170,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10171,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4671,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10172,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10173,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4672,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10174,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10175,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4673,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10176,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10177,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4674,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10178,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10179,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 10180,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4675,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10181,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10182,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10183,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4676,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10184,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10185,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Para Choque Tras",
        #         "estaOk": True,
        #         "codigoModelo": 4677,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10186,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4678,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10187,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10188,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10189,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4679,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10190,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 10191,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4680,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10192,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10193,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4681,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10194,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10195,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4682,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10196,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10197,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4683,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10198,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10199,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4684,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10200,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10201,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10202,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4685,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10203,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10204,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 13319,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 5381,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 13320,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 13321,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10205,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4686,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10206,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10207,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Roda Estepe",
        #         "estaOk": True,
        #         "codigoModelo": 4687,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [{
        #                 "codigo": 4688,
        #                 "descricao": "Modelo",
        #                 "obrigatorio": False,
        #                 "visivel": True,
        #                 "ordem": 0,
        #                 "listaResposta": [{
        #                     "descricao": "Ferro",
        #                     "valor": "",
        #                     "codigoPergunta": 10208,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Liga Leve",
        #                     "valor": "",
        #                     "codigoPergunta": 10209,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }]
        #             }],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10210,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4696,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10226,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 13322,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10213,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4689,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10211,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10212,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10215,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4690,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10214,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10217,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4691,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10216,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10219,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4692,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10218,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10221,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4693,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10220,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 10223,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4694,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10222,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10225,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4695,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10224,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Sup Bagagito DD",
        #         "estaOk": True,
        #         "codigoModelo": 4424,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9601,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4425,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9602,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9603,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desgastado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9604,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4426,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9605,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9606,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9607,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4427,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9608,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9609,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4428,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9610,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9611,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9612,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4429,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9613,
        #                 "descricao": "Limpar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9614,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9615,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4430,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9616,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9617,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4431,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9618,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9619,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Rasgado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9620,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4432,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9621,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9622,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Sup Bagagito DE",
        #         "estaOk": True,
        #         "codigoModelo": 4433,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9623,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4434,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9624,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9625,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desgastado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9626,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4435,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9627,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9628,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9629,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4436,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9630,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9631,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4437,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9632,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9633,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9634,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4438,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9635,
        #                 "descricao": "Limpar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9636,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9637,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4439,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9638,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9639,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4440,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9640,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9641,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Rasgado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9642,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4441,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9643,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9644,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Tampa Tras",
        #         "estaOk": None,
        #         "codigoModelo": 4697,
        #         "item": {
        #             "obrigatorio": True,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Adesivado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10227,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4698,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10228,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10229,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10230,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4699,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10231,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10232,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10233,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4700,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10234,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10235,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10236,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4701,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10237,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10238,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4702,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10239,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 10240,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4703,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10241,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10242,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10243,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4704,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10244,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10245,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4705,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10246,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10247,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4706,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10248,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10249,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 10250,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4707,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10251,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10252,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10253,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4708,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10254,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10255,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Tapete Mala",
        #         "estaOk": True,
        #         "codigoModelo": 4450,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9660,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4451,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9661,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desgastado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9662,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4452,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9663,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 9664,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4453,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9665,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9666,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4454,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9667,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9668,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4455,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9669,
        #                 "descricao": "Limpar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 9670,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 9671,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4456,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9672,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Rasgado",
        #             "valorProblema": "",
        #             "codigoPergunta": 9673,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4457,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 9674,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Vidro Vigia",
        #         "estaOk": True,
        #         "codigoModelo": 4709,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10256,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4710,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10257,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10258,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4711,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10259,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10260,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10261,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4712,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10262,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10263,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10264,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4713,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10265,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10266,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Outros",
        #         "estaOk": True,
        #         "codigoModelo": 4665,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 2,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10159,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 5380,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 13318,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }]
        #     }],
        #     "ehParteDesenho": True,
        #     "codigoParte": 4609
        # }, {
        #     "parte": "Traseira Direita",
        #     "habilitadoEdicao": True,
        #     "listaItemResposta": [{
        #         "descricaoItem": "Caixa de Roda TD",
        #         "estaOk": True,
        #         "codigoModelo": 4720,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10277,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4721,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10278,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10279,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10280,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4722,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10281,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10282,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10283,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4723,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10284,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10285,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4724,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10286,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 10287,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4725,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10288,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10289,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10290,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4726,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10291,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10292,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4727,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10293,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10294,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4728,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10295,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10296,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 10297,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4729,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10298,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10299,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10300,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4730,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10301,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10302,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Calota TD",
        #         "estaOk": True,
        #         "codigoModelo": 4731,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10303,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4732,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10304,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10305,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10306,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4733,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10307,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10308,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10309,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4734,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10310,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10311,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10321,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4738,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10322,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10312,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4735,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10313,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10314,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10315,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4736,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10316,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10317,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10318,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4737,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10319,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10320,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Entrada de Porta TD",
        #         "estaOk": True,
        #         "codigoModelo": 4739,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10323,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4740,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10324,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10325,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10326,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4741,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10327,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10328,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10329,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4742,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10330,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10331,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4743,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10332,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 10333,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4744,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10334,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10335,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10336,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4745,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10337,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10338,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4746,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10339,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10340,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4747,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10341,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10342,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 10343,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4748,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10344,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10345,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10346,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4749,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10347,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10348,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Forro de Porta TD",
        #         "estaOk": True,
        #         "codigoModelo": 4750,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10349,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4751,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10350,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10351,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10352,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4752,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10353,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10354,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desfiado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10355,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4753,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10356,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10357,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 10358,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4754,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10359,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10360,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4755,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10361,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10362,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10363,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4756,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10364,
        #                 "descricao": "Limpar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10365,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10366,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4757,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10367,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10368,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4758,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10369,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10370,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 10371,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4759,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10372,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10373,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Friso/Borrachão Dir",
        #         "estaOk": True,
        #         "codigoModelo": 4760,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Avariado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10374,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4761,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10375,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10376,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desalinhado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10377,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4762,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10378,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10379,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 10380,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4763,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10381,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10382,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4764,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10383,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 10384,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4765,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10385,
        #                 "descricao": "Fixar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10386,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Guarnição TD",
        #         "estaOk": True,
        #         "codigoModelo": 4766,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10387,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4767,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10388,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10389,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4768,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10390,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10391,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 10392,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4769,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10393,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10394,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4770,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10395,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10396,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4771,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10397,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10398,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10399,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4772,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10400,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 10401,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4773,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10402,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10403,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Insulfilm TD",
        #         "estaOk": True,
        #         "codigoModelo": 4774,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Avariado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10404,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4775,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10405,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10406,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10407,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4776,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10408,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Lanterna Dir",
        #         "estaOk": True,
        #         "codigoModelo": 4777,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 10409,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4778,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10410,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Infiltração",
        #             "valorProblema": "",
        #             "codigoPergunta": 10411,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4779,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10412,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10413,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10414,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4780,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10415,
        #                 "descricao": "outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10416,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4781,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10417,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10418,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10419,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4782,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10420,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10421,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10422,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4783,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10423,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10424,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Trincado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10425,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4784,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10426,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10427,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Lateral Direita",
        #         "estaOk": True,
        #         "codigoModelo": 4785,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Adesivado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10428,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4786,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10429,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10430,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10431,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4787,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10432,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10433,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10434,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4788,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10435,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10436,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10437,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4789,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10438,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10439,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4790,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10440,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 10441,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4791,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10442,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10443,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10444,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4792,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10445,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10446,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4793,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10447,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10448,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4794,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10449,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10450,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 10451,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4795,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10452,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10453,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10454,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4796,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10455,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10456,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Maçaneta TD",
        #         "estaOk": True,
        #         "codigoModelo": 4797,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10457,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4798,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10458,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 10459,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4799,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10460,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Abre",
        #             "valorProblema": "",
        #             "codigoPergunta": 10461,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4800,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10462,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10463,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10464,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4801,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10465,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10466,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4802,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10467,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10468,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10469,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4803,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10470,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10471,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 10472,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4804,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10473,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10474,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10475,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4805,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10476,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10477,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Porta TD",
        #         "estaOk": None,
        #         "codigoModelo": 4807,
        #         "item": {
        #             "obrigatorio": True,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Adesivado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10479,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4808,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10480,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10481,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10482,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4809,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10483,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10484,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10485,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4810,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10486,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10487,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10488,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4811,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10489,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10490,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4812,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10491,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 10492,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4813,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10493,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10494,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10495,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4814,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10496,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10497,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4815,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10498,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10499,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4816,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10500,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10501,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 10502,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4817,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10503,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10504,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10505,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4818,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10506,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10507,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Roda TD",
        #         "estaOk": True,
        #         "codigoModelo": 4819,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [{
        #                 "codigo": 4820,
        #                 "descricao": "Modelo",
        #                 "obrigatorio": False,
        #                 "visivel": True,
        #                 "ordem": 0,
        #                 "listaResposta": [{
        #                     "descricao": "Ferro",
        #                     "valor": "",
        #                     "codigoPergunta": 10508,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Liga Leve",
        #                     "valor": "",
        #                     "codigoPergunta": 10509,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }]
        #             }],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10510,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4828,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10526,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 13324,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10513,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4821,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10511,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10512,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10515,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4822,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10514,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10517,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4823,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10516,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10519,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4824,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10518,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10521,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4825,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10520,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 10523,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4826,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10522,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10525,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4827,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10524,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Tanque Combustivel",
        #         "estaOk": True,
        #         "codigoModelo": 3857,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8301,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3858,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8302,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8303,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 8304,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3859,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8305,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8306,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3860,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8307,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8308,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Trincado",
        #             "valorProblema": "",
        #             "codigoPergunta": 8309,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3861,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8310,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 8311,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Vazamento",
        #             "valorProblema": "",
        #             "codigoPergunta": 8312,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 3862,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 8313,
        #                 "descricao": "Verificar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Vidro porta TD",
        #         "estaOk": True,
        #         "codigoModelo": 4829,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10527,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4830,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10528,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10529,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4831,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10530,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10531,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10532,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4832,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10533,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10534,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10535,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4833,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10536,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10537,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Vidro Vigia TD",
        #         "estaOk": True,
        #         "codigoModelo": 5383,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 13325,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 5384,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 13326,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 13327,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 5385,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 13328,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 13329,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 13330,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 5386,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 13331,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 13332,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 13333,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 5387,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 13334,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 13335,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Outros",
        #         "estaOk": True,
        #         "codigoModelo": 4806,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 2,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10478,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 5382,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 13323,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }]
        #     }],
        #     "ehParteDesenho": True,
        #     "codigoParte": 4714
        # }, {
        #     "parte": "Traseira Esquerda",
        #     "habilitadoEdicao": True,
        #     "listaItemResposta": [{
        #         "descricaoItem": "Caixa de Roda TE",
        #         "estaOk": True,
        #         "codigoModelo": 4840,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10548,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4841,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10549,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10550,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10551,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4842,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10552,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10553,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10554,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4843,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10555,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10556,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4844,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10557,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 10558,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4845,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10559,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10560,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10572,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4850,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10573,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10561,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4846,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10562,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10563,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4847,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10564,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10565,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 10566,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4848,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10567,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10568,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10569,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4849,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10570,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10571,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Calota TE",
        #         "estaOk": True,
        #         "codigoModelo": 4851,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10574,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4852,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10575,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10576,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10577,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4853,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10578,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10579,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10580,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4854,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10581,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10582,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10592,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4858,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10593,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10583,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4855,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10584,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10585,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10586,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4856,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10587,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10588,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10589,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4857,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10590,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10591,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Entrada de Porta TE",
        #         "estaOk": True,
        #         "codigoModelo": 4859,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10594,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4860,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10595,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10596,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10597,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4861,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10598,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10599,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10600,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4862,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10601,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10602,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4863,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10603,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 10604,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4864,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10605,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10606,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10618,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4869,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10619,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10607,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4865,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10608,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10609,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4866,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10610,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10611,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 10612,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4867,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10613,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10614,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10615,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4868,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10616,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10617,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Forro de Porta TE",
        #         "estaOk": True,
        #         "codigoModelo": 4870,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10620,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4871,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10621,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10622,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10623,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4872,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10624,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10625,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desfiado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10626,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4873,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10627,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10628,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 10629,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4874,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10630,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10631,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4875,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10632,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10633,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10634,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4876,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10635,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10636,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10643,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4879,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10644,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10637,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4877,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10638,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10639,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 10640,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4878,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10641,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10642,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Friso/Borrachão Esq",
        #         "estaOk": True,
        #         "codigoModelo": 4880,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Avariado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10645,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4881,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10646,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10647,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Desalinhado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10648,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4882,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10649,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10650,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 10651,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4883,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10652,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10656,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4885,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10657,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 10653,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4884,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10654,
        #                 "descricao": "Fixar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10655,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Guarnição TE",
        #         "estaOk": True,
        #         "codigoModelo": 4886,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Cortado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10658,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4887,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10659,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10660,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4888,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10661,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10662,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 10663,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4889,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10664,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10665,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4890,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10666,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Manchado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10667,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4891,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10668,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10669,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10673,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4893,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10674,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Solto",
        #             "valorProblema": "",
        #             "codigoPergunta": 10670,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4892,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10671,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10672,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Insulfilm TE",
        #         "estaOk": True,
        #         "codigoModelo": 4894,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Avariado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10675,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4895,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10676,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10677,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10678,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4896,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10679,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Lanterna Esq",
        #         "estaOk": True,
        #         "codigoModelo": 4897,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 10680,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4898,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10681,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Infiltração",
        #             "valorProblema": "",
        #             "codigoPergunta": 10682,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4899,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10683,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10684,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10697,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4904,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10698,
        #                 "descricao": "outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10685,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4900,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10686,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10687,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10688,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4901,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10689,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10690,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10691,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4902,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10692,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10693,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Trincado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10694,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4903,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10695,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10696,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Lateral Esquerda",
        #         "estaOk": True,
        #         "codigoModelo": 4905,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Adesivado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10699,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4906,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10700,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10701,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10702,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4907,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10703,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10704,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10705,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4908,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10706,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10707,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10708,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4909,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10709,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10710,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4910,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10711,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 10712,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4911,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10713,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10714,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10726,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4916,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10727,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10715,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4912,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10716,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10717,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4913,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10718,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10719,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 10720,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4914,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10721,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10722,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10723,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4915,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10724,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10725,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Maçaneta TE",
        #         "estaOk": True,
        #         "codigoModelo": 4917,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10728,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4918,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10729,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Faltante",
        #             "valorProblema": "",
        #             "codigoPergunta": 10730,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4919,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10731,
        #                 "descricao": "Repor",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Não Abre",
        #             "valorProblema": "",
        #             "codigoPergunta": 10732,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4920,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10733,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10734,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10747,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4925,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10748,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10735,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4921,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10736,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10737,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10738,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4922,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10739,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10740,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 10741,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4923,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10742,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10743,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10744,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4924,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10745,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10746,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Porta TE",
        #         "estaOk": None,
        #         "codigoModelo": 4927,
        #         "item": {
        #             "obrigatorio": True,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Adesivado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10750,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4928,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10751,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10752,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10753,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4929,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10754,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10755,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10756,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4930,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10757,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10758,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10759,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4931,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10760,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Furado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10761,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4932,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10762,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Mossas",
        #             "valorProblema": "",
        #             "codigoPergunta": 10763,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4933,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10764,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10765,
        #                 "descricao": "Martelinho",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10777,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4938,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10778,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10766,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4934,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10767,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10768,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4935,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10769,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10770,
        #                 "descricao": "Pincelar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 10771,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4936,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10772,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10773,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10774,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4937,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10775,
        #                 "descricao": "Funilaria/Pintura",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10776,
        #                 "descricao": "Polir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Roda TE",
        #         "estaOk": True,
        #         "codigoModelo": 4939,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [{
        #                 "codigo": 4940,
        #                 "descricao": "Modelo",
        #                 "obrigatorio": False,
        #                 "visivel": True,
        #                 "ordem": 0,
        #                 "listaResposta": [{
        #                     "descricao": "Ferro",
        #                     "valor": "",
        #                     "codigoPergunta": 10779,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }, {
        #                     "descricao": "Liga Leve",
        #                     "valor": "",
        #                     "codigoPergunta": 10780,
        #                     "resposta": False,
        #                     "executarServico": True,
        #                     "codigoSolucao": 0,
        #                     "codigoRespostaResposta": None,
        #                     "listaSolucao": []
        #                 }]
        #             }],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Amassado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10781,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4948,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10797,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 13337,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Contaminado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10784,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4941,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10782,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10783,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Descascado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10786,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4942,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10785,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10796,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4947,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10795,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Oxidado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10788,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4943,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10787,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10790,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4944,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10789,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Reparo Defeituoso",
        #             "valorProblema": "",
        #             "codigoPergunta": 10792,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4945,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10791,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10794,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4946,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10793,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Vidro Porta TE",
        #         "estaOk": True,
        #         "codigoModelo": 4949,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10807,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4953,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10808,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 10798,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4950,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10799,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10800,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 10801,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4951,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10802,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10803,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 10804,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 4952,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 10805,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 10806,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Vidro Vigia TE",
        #         "estaOk": True,
        #         "codigoModelo": 5389,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 13338,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 5390,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 13339,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Piques",
        #             "valorProblema": "",
        #             "codigoPergunta": 13340,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 5391,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 13341,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 13342,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Quebrado",
        #             "valorProblema": "",
        #             "codigoPergunta": 13343,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 5392,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 13344,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 13345,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "Risco com dano",
        #             "valorProblema": "",
        #             "codigoPergunta": 13346,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 5393,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 13347,
        #                 "descricao": "Recuperar",
        #                 "resposta": False
        #             }, {
        #                 "codigo": 13348,
        #                 "descricao": "Substituir",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "Outros",
        #         "estaOk": True,
        #         "codigoModelo": 4926,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 2,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Outros",
        #             "valorProblema": "",
        #             "codigoPergunta": 10749,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 5388,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 13336,
        #                 "descricao": "Outros",
        #                 "resposta": False
        #             }]
        #         }]
        #     }],
        #     "ehParteDesenho": True,
        #     "codigoParte": 4834
        # }, {
        #     "parte": "Itens Específicos",
        #     "habilitadoEdicao": True,
        #     "listaItemResposta": [{
        #         "descricaoItem": "Lavagem",
        #         "estaOk": None,
        #         "codigoModelo": 6693,
        #         "item": {
        #             "obrigatorio": True,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Especial",
        #             "valorProblema": "",
        #             "codigoPergunta": 16341,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 0,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": []
        #         }, {
        #             "descricaoProblema": "Simples",
        #             "valorProblema": "",
        #             "codigoPergunta": 16342,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 0,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": []
        #         }]
        #     }, {
        #         "descricaoItem": "Polimento",
        #         "estaOk": True,
        #         "codigoModelo": 6694,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": True,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "Enceramento",
        #             "valorProblema": "",
        #             "codigoPergunta": 16343,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 0,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": []
        #         }, {
        #             "descricaoProblema": "Tecnico com lixa",
        #             "valorProblema": "",
        #             "codigoPergunta": 16344,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 0,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": []
        #         }]
        #     }, {
        #         "descricaoItem": "CHECK MECANICO",
        #         "estaOk": None,
        #         "codigoModelo": 6734,
        #         "item": {
        #             "obrigatorio": True,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": False,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "CHECK MECANICO",
        #             "valorProblema": "",
        #             "codigoPergunta": 16435,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6735,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16436,
        #                 "descricao": "AGENDAR",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "MOTOR",
        #         "estaOk": True,
        #         "codigoModelo": 6736,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": False,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "BARULHO",
        #             "valorProblema": "",
        #             "codigoPergunta": 16437,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6737,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16438,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "CARTER AVARIADO",
        #             "valorProblema": "",
        #             "codigoPergunta": 16486,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6771,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16487,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "CARTER VAZAMENTO",
        #             "valorProblema": "",
        #             "codigoPergunta": 16488,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6772,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16489,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "FALHANDO",
        #             "valorProblema": "",
        #             "codigoPergunta": 16439,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6738,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16440,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "NÃO FUNCIONA",
        #             "valorProblema": "",
        #             "codigoPergunta": 16441,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6739,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16442,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "OUTROS",
        #             "valorProblema": "",
        #             "codigoPergunta": 16445,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6741,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16446,
        #                 "descricao": "OUTROS",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "VAZAMENTO",
        #             "valorProblema": "",
        #             "codigoPergunta": 16443,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6740,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16444,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "SUSPENSAO DIANTEIRA ",
        #         "estaOk": True,
        #         "codigoModelo": 6743,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": False,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "AVARIADA",
        #             "valorProblema": "",
        #             "codigoPergunta": 16448,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6744,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16449,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "BARULHO",
        #             "valorProblema": "",
        #             "codigoPergunta": 16450,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6745,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16451,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "OUTROS",
        #             "valorProblema": "",
        #             "codigoPergunta": 16452,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6746,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16453,
        #                 "descricao": "OUTROS",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "SEM ESTABILIDADE",
        #             "valorProblema": "",
        #             "codigoPergunta": 16454,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6747,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16455,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "SUSPENSAO TRASEIRA ",
        #         "estaOk": True,
        #         "codigoModelo": 6748,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": False,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "AVARIADA",
        #             "valorProblema": "",
        #             "codigoPergunta": 16456,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6749,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16457,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "BARULHO",
        #             "valorProblema": "",
        #             "codigoPergunta": 16458,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6750,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16459,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "OUTROS",
        #             "valorProblema": "",
        #             "codigoPergunta": 16460,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6751,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16461,
        #                 "descricao": "OUTROS",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "SEM ESTABILIDADE",
        #             "valorProblema": "",
        #             "codigoPergunta": 16462,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6752,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16463,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "FREIO",
        #         "estaOk": True,
        #         "codigoModelo": 6753,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": False,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "AVARIADO",
        #             "valorProblema": "",
        #             "codigoPergunta": 16464,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6754,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16465,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "BARULHO",
        #             "valorProblema": "",
        #             "codigoPergunta": 16466,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6755,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16467,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "FALHANDO",
        #             "valorProblema": "",
        #             "codigoPergunta": 16468,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6756,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16469,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "OUTROS",
        #             "valorProblema": "",
        #             "codigoPergunta": 16470,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6757,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16471,
        #                 "descricao": "OUTROS",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "EMBREAGEM",
        #         "estaOk": True,
        #         "codigoModelo": 6758,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": False,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "BARULHO",
        #             "valorProblema": "",
        #             "codigoPergunta": 16472,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6759,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16473,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "OUTROS",
        #             "valorProblema": "",
        #             "codigoPergunta": 16476,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6761,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16477,
        #                 "descricao": "OUTROS",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "TREPIDANDO",
        #             "valorProblema": "",
        #             "codigoPergunta": 16474,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6760,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16475,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "ROLAMENTO RODA D/D",
        #         "estaOk": True,
        #         "codigoModelo": 6762,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": False,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "BARULHO",
        #             "valorProblema": "",
        #             "codigoPergunta": 16478,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6763,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16479,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "ROLAMENTO RODA D/E",
        #         "estaOk": True,
        #         "codigoModelo": 6764,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": False,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "BARULHO",
        #             "valorProblema": "",
        #             "codigoPergunta": 16480,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6765,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16481,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "ROLAMENTO RODA T/D",
        #         "estaOk": True,
        #         "codigoModelo": 6766,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": False,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "BARULHO",
        #             "valorProblema": "",
        #             "codigoPergunta": 16482,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6767,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16483,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "ROLAMENTO RODA T/E",
        #         "estaOk": True,
        #         "codigoModelo": 6769,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": False,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "BARULHO",
        #             "valorProblema": "",
        #             "codigoPergunta": 16484,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6770,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16485,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "PROTETOR DE CARTER",
        #         "estaOk": True,
        #         "codigoModelo": 6773,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": False,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "AVARIADO",
        #             "valorProblema": "",
        #             "codigoPergunta": 16490,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6774,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16491,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "BARULHO",
        #             "valorProblema": "",
        #             "codigoPergunta": 16492,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6775,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16493,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "FALTANTE \"NAO DISPONIBILIZADO\"",
        #             "valorProblema": "",
        #             "codigoPergunta": 16494,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6776,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16495,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "OUTROS",
        #             "valorProblema": "",
        #             "codigoPergunta": 16496,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6777,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16497,
        #                 "descricao": "OUTROS",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "AMORTECEDOR DIANT",
        #         "estaOk": True,
        #         "codigoModelo": 6778,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": False,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "AVARIADO",
        #             "valorProblema": "",
        #             "codigoPergunta": 16500,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6780,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16501,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "BARULHO",
        #             "valorProblema": "",
        #             "codigoPergunta": 16498,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6779,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16499,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "OUTROS",
        #             "valorProblema": "",
        #             "codigoPergunta": 16502,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6781,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16503,
        #                 "descricao": "OUTROS",
        #                 "resposta": False
        #             }]
        #         }]
        #     }, {
        #         "descricaoItem": "AMORTECEDOR TRAS",
        #         "estaOk": True,
        #         "codigoModelo": 6782,
        #         "item": {
        #             "obrigatorio": False,
        #             "visivel": True,
        #             "ordem": 0,
        #             "permiteFoto": False,
        #             "obrigaFoto": False,
        #             "obrigaObservacao": False,
        #             "listaFoto": [],
        #             "observacao": "",
        #             "listaCaracteristicas": [],
        #             "existeFoto": False
        #         },
        #         "listaRespostas": [{
        #             "descricaoProblema": "AVARIADO",
        #             "valorProblema": "",
        #             "codigoPergunta": 16506,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6784,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16507,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "BARULHO",
        #             "valorProblema": "",
        #             "codigoPergunta": 16504,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6783,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16505,
        #                 "descricao": "VERIFICAR",
        #                 "resposta": False
        #             }]
        #         }, {
        #             "descricaoProblema": "OUTROS",
        #             "valorProblema": "",
        #             "codigoPergunta": 16508,
        #             "respostaProblema": False,
        #             "executarServico": True,
        #             "codigoSolucao": 6785,
        #             "codigoRespostaResposta": None,
        #             "listaSolucao": [{
        #                 "codigo": 16509,
        #                 "descricao": "OUTROS",
        #                 "resposta": False
        #             }]
        #         }]
        #     }],
        #     "ehParteDesenho": False,
        #     "codigoParte": 6692
        # }],
        # "listaChecklist": []
        }],
        "opstatus": 0,
        "httpStatusCode": 200
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5001')