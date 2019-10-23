/* 
Crie um Analisador Léxico utilizando Flex que consiga gerar os tokens
do arquivo de entrada "exercicio01.in" que consiste em um código na
linguagem C. O analisador deverá identificar todos os tokens referentes a:

1. Identificadores
2. Números Inteiros
3. Números de Ponto Flutuante
4. Palavras reservadas
5. Operadores Matemáticos e Relacionais
6. Chaves, Colchetes e Chaves

utilize os exemplos no diretório "flex" como ponto de partida.
*/

%{
    /*
        Definições que estarão disponíveis 
            - variáveis
            - constantes
        O que for aqui será copiado para o arquivo *.yy.c
    
        Variáveis declaradas aqui estarão acessível nas funções yylex() e 
        main().
    */
    int contador = 0;
%}

/* Definições de Nomes */
IDENTIFICADOR   [_a-zA-Z][_a-zA-Z0-9]*  

/* FIM DA SEÇÃO DE DEFINIÇÕES */

%%
    /* SEÇAO DE REGRAS 
        Uma entrada por linha no formato:
        
        padrão  ação
    */
[0-9]+              {printf("<number, %s>", yytext);}
>|<|>=|<=|==|!=     {printf("<op_rel, %s>", yytext);}                                      
int|float           {printf("<plavra_reservada, %s>", yytext); contador++;}
{IDENTIFICADOR}     {printf("<identificador, %s>", yytext); contador++;}
\+                   {printf("<soma,>"); contador++;}
<<EOF>>             return 0;
    
%%
/*
Seção de Código do Usuário
*/
int yywrap() {}
int main() {
    printf("Iniciando Análise Léxica...\n---\n");
    yylex();
    printf("Foram encontradas %d ocorrências de identificadores.\n", contador);
    printf("---\nÁnalise Finalizada!\n");
    
    return 0;
}
