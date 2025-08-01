from sklearn.utils import Bunch
from sklearn.feature_extraction.text import TfidfVectorizer
def load_questions (): 
    vetor = TfidfVectorizer()
    perguntas = [
        "O que é inteligência artificial?",
        "Explique a diferença entre aprendizado supervisionado e não supervisionado.",
        "Quais são os principais componentes de um computador?",
        "Como funciona o protocolo HTTP?",
        "O que significa o conceito de recursão em programação?",
        "Qual a importância da normalização em bancos de dados?",
        "Descreva o funcionamento de uma árvore binária de busca.",
        "O que é o algoritmo de Dijkstra e para que ele serve?",
        "Quais as vantagens e desvantagens do uso de blockchain?",
        "Como a análise de sentimentos pode ser aplicada em redes sociais?",
        "Qual a função do sistema operacional em um computador?",
        "Por que a modularização é importante no desenvolvimento de software?",
        "O que é overfitting em modelos de machine learning?",
        "Explique como funciona o DNS na internet.",
        "Como o modelo cliente-servidor organiza uma rede?",
        "O que caracteriza uma linguagem de programação funcional?",
        "Quais são os principais tipos de banco de dados?",
        "Qual a diferença entre memória RAM e ROM?",
        "Como funcionam os algoritmos genéticos?",
        "Por que o tempo de complexidade é importante na análise de algoritmos?",
        "O que é um interpretador em linguagens de programação?",
        "Como funcionam os containers Docker?",
        "Explique o conceito de variáveis aleatórias em estatística.",
        "Qual a diferença entre IPv4 e IPv6?",
        "Como o garbage collector atua em linguagens como Java ou Python?",
        "O que são redes neurais convolucionais (CNN)?",
        "Para que serve um firewall em redes de computadores?",
        "O que é paralelismo e como ele é usado em processamento de dados?",
        "Qual o papel do protocolo TCP na comunicação entre computadores?",
        "Explique o conceito de classe e objeto na programação orientada a objetos."
    ]

    rotulos_target_names = [
        "simples",
        "complexa",
        "acessível",
        "abstrata",
        "longa demais"
    ]

    rotulos_target = [
        0,  # inteligência artificial
        1,  # aprendizado supervisionado vs não supervisionado
        2,  # componentes do computador
        0,  # protocolo HTTP
        3,  # recursão
        1,  # normalização em BD
        2,  # árvore binária
        3,  # Dijkstra
        4,  # blockchain
        4,  # análise de sentimentos
        0,  # sistema operacional
        1,  # modularização
        3,  # overfitting
        1,  # DNS
        2,  # cliente-servidor
        3,  # linguagem funcional
        2,  # tipos de BD
        0,  # RAM vs ROM
        3,  # algoritmos genéticos
        3,  # complexidade
        0,  # interpretador
        2,  # Docker
        3,  # variáveis aleatórias
        2,  # IPv4 vs IPv6
        3,  # garbage collector
        3,  # CNN
        1,  # firewall
        3,  # paralelismo
        1,  # TCP
        2   # classe e objeto
    ]
    return Bunch(
        perguntas=perguntas,
        rotulos_target_names=rotulos_target_names,
        rotulos_target=rotulos_target
    #     "perguntas": [
    #         "O que é inteligência artificial?",
    #         "Explique a diferença entre aprendizado supervisionado e não supervisionado.",
    #         "Quais são os principais componentes de um computador?",
    #         "Como funciona o protocolo HTTP?",
    #         "O que significa o conceito de recursão em programação?",
    #         "Qual a importância da normalização em bancos de dados?",
    #         "Descreva o funcionamento de uma árvore binária de busca.",
    #         "O que é o algoritmo de Dijkstra e para que ele serve?",
    #         "Quais as vantagens e desvantagens do uso de blockchain?",
    #         "Como a análise de sentimentos pode ser aplicada em redes sociais?"
    #     ],
    #     "rotulos_target_names": [
    #         "simples",
    #         "complexa",
    #         "acessível",
    #         "abstrata",
    #         "longa demais"
    #     ],
    #     "rotulos_target": [

    #         0,
    #         1,
    #         2,
    #         0,
    #         3,
    #         1,
    #         2,
    #         3,
    #         4,
    #         4
    # ]

    )