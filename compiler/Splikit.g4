grammar Splikit;

parse: stmt* EOF;

type: ID (LBRACK ID RBRACK)?;

stmt: varAssign | funcAssign | ifStmt | whileStmt | useStmt | expr;

bodyStmts: stmt | RETURN expr;
body: LBRACE bodyStmts* RBRACE;

ifStmt
    : IF expr body elseifStmt* elseStmt?
    | IF LPAREN expr RPAREN body elseifStmt* elseStmt?
    ;
elseifStmt
    : ELSE IF expr body
    | ELSE IF LPAREN expr RPAREN body
    ;
elseStmt: ELSE body;
whileStmt: WHILE expr body;
useStmt: USE STRING (COMMA STRING)*;

funcAssign: INLINE? FUNC ID LPAREN params? RPAREN (RETURNS type)? body;
varAssign
    : CONST? type? ID ASSIGN expr
    | ID (ADD | SUB | MUL | DIV | MOD) ASSIGN expr
    | ID (INCREMENT | DECREMENT)
    ;

arg: expr;
args: arg (COMMA arg)*;

param: type ID;
params: param (COMMA param)*;

call: ID LPAREN args? RPAREN;
atom: INT | FLOAT | STRING | BOOL | NIL | ID | LPAREN expr RPAREN | type LBRACE args? RBRACE;

expr
    : call
    | expr DOT ID (LPAREN args? RPAREN)?
    | atom
    | NOT expr
    | expr op=(ADD | SUB) expr
    | expr op=(MUL | DIV | MOD) expr
    | expr op=(EEQ | NEQ | GT | LT | GTE | LTE) expr
    | expr op=(AND | OR) expr
    ;


IF: 'if';
USE: 'use';
ELSE: 'else';
FUNC: 'func';
CONST: 'const';
WHILE: 'while';
INLINE: 'inline';
RETURN: 'return';

INT: '-'? [0-9]+;
FLOAT: '-'? [0-9]* '.' [0-9]+;
APOSTROPHE: '\'';
STRING: '"' .*? '"' | APOSTROPHE .*? APOSTROPHE;
BOOL: 'true' | 'false';
NIL: 'nil';
ID: [a-zA-Z_][a-zA-Z_0-9]*;

INCREMENT: '++';
DECREMENT: '--';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EEQ: '==';
NEQ: '!=';
GT: '>';
LT: '<';
GTE: '>=';
LTE: '<=';
AND: '&&';
OR: '||';
NOT: '!';

DOT: '.';
COMMA: ',';
ASSIGN: '=';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACK: '[';
RBRACK: ']';
RETURNS: '->';

COMMENT: '//' .*? '\n' -> skip;
MULTILINE: '/*' .*? '*/' -> skip;
WHITESPACE: [\t\r\n ]+ -> skip;
