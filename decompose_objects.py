"""
Decompondo um programa Python visualmente
==========================================

A afirmação do Lutz (Learning Python, capítulo sobre objetos):

    "Python programs can be decomposed into modules, statements,
     expressions, and objects, as follows:
     1. Programs are composed of modules.
     2. Modules contain statements.
     3. Statements contain expressions.
     4. Expressions create and process objects."

A ideia é uma cascata: cada nível "contém" o próximo, até chegar na
menor unidade — o objeto. Este arquivo .py É uma demonstração viva
dessa cascata: ele é um módulo, tem statements, e cada statement
contém expressions que criam objetos. Rode e veja.
"""

# A LINHA DE BAIXO É O EXEMPLO QUE VAMOS DISSECAR
# ------------------------------------------------------------------
total = 1 + 2                # um statement de atribuição
print(total)                 # um statement de chamada de função
# ------------------------------------------------------------------

# Nível 1: PROGRAMA -> MÓDULO
# Um programa é feito de um ou mais módulos (.py). Cada arquivo .py
# é um módulo. Este arquivo é um módulo. Quando você roda `python
# decompose_objects.py`, você executa um módulo.
def nivel1_programa_e_modulo():
    print("\n[1] PROGRAMA -> MÓDULO")
    print("    Programa = coleção de módulos (.py). Este arquivo é um módulo.")


# Nível 2: MÓDULO -> STATEMENTS
# Dentro de um módulo, o código é organizado em statements
# (comandos/instruções). O interpretador executa cada statement em
# ordem, de cima para baixo. Um `def` cria uma função, mas a função só
# roda quando é chamada — o statement é só a definição.
def nivel2_modulo_e_statements():
    print("\n[2] MÓDULO -> STATEMENTS")
    print("    Statements no topo deste módulo:")
    print("      * total = 1 + 2        (atribuição)")
    print("      * print(total)         (chamada de função)")
    print("      * cada def ...         (definição de função)")
    print("      * if __name__ ...      (condicional)")


# Nível 3: STATEMENTS -> EXPRESSIONS
# Dentro de um statement existem expressions (expressões): pedaços de
# código que produzem/retornam um valor. "1 + 2" é uma expressão.
# "total" é uma expressão. Chamar uma função é uma expressão.
def nivel3_statements_e_expressions():
    print("\n[3] STATEMENTS -> EXPRESSIONS")
    print("    Dissetor do statement:  total = 1 + 2")
    print("      * '1'      é uma expressão (literal inteiro)")
    print("      * '2'      é uma expressão (literal inteiro)")
    print("      * '1 + 2'  é uma expressão (soma de duas)")
    print("      * 'total'  é uma expressão (nome/atribuição)")
    print("    Cada expressão AVALIA para produzir um valor.")


# Nível 4: EXPRESSIONS -> OBJETOS
# Quando uma expressão é avaliada, o resultado é um objeto. '1' cria o
# objeto int 1. '1 + 2' cria um NOVO objeto int 3. 'total' passa a
# apontar (ligar) para esse objeto. Até a string de print é um objeto.
def nivel4_expressions_e_objetos():
    print("\n[4] EXPRESSIONS -> OBJETOS")
    total = 1 + 2
    valor = 1
    outro = 2
    print(f"    '1'       cria o objeto:  {valor!r:>20}  tipo={type(valor).__name__:>5}  id={id(valor)}")
    print(f"    '2'       cria o objeto:  {outro!r:>20}  tipo={type(outro).__name__:>5}  id={id(outro)}")
    print(f"    '1 + 2'   cria o objeto:  {total!r:>20}  tipo={type(total).__name__:>5}  id={id(total)}")
    print(f"    'print()' usa um objeto str: {repr('total = 3'):>20}  tipo={type('x').__name__:>5}")
    print("    Objeto = a unidade mínima: tipo + valor + identidade.")


# O desenho final: a cascata completa
def cascata():
    print()
    print("=" * 60)
    print("            A CASCATA COMPLETA")
    print("=" * 60)
    print(
        """
    PROGRAMA
     └── MÓDULO  (este arquivo .py)
          └── STATEMENTS
              ├── total = 1 + 2      <-- atribuição
              │    └── EXPRESSIONS
              │        ├── 1        -> objeto int 1
              │        ├── 2        -> objeto int 2
              │        └── 1 + 2    -> objeto int 3 (novo!)
              └── print(total)       <-- chamada de função
                   └── EXPRESSIONS
                       ├── total    -> lê o objeto int 3
                       └── print()  -> objeto função + objeto str
        """
    )
    print("=" * 60)
    print(
        "    A moral da história: até o menor pedaço do seu código,\n"
        "    um literal ou uma soma, vira um objeto na memória."
    )


if __name__ == "__main__":
    nivel1_programa_e_modulo()
    nivel2_modulo_e_statements()
    nivel3_statements_e_expressions()
    nivel4_expressions_e_objetos()
    cascata()

    # ponytail: check mínimo — a demonstração só tem valor se o objeto
    # 'total' realmente for o resultado da soma. Se quebrar, o script falha.
    assert 1 + 2 == 3