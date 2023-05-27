grammar Splikit;

program: statement*;

statement: variableDeclaration
         | functionDeclaration
         | ifStatement
         | whileStatement
         | importStatement
         | enumDeclaration
         | classDeclaration
         | expression
         ;

variableDeclaration: Identifier '=' expression;

functionDeclaration
    : 'func' Identifier ('::' Identifier)? '(' parameterList? ')' '{' statement* '}'
    | Identifier '(' parameterList? ')' '=>' '{' statement* '}'
    ;

enumDeclaration: 'enum' Identifier '{' variableDeclaration* '}';

clsFuncDeclaration: 'func' Identifier '(' parameterList? ')' '{' statement* '}';

classDeclarations
    : (clsFuncDeclaration | variableDeclaration)*
    ;

classDeclaration: 'class' Identifier '{' classDeclarations '}';

functionCall: Identifier '(' argumentList? ')';

ifStatement: 'if' expression '{' statement* '}' ('else' '{' statement* '}')?;
importStatement: 'import' ('{' StringLiteral (',' StringLiteral)* '}' | '*')? StringLiteral;
whileStatement: 'while' expression '{' statement* '}';

parameterList: Identifier (',' Identifier)*;

argumentList: expression (',' expression)*;

getAttr: primaryExpression ('.' Identifier ('(' argumentList? ')')?)+;
expression
    : primaryExpression (operator expression)*
    | '!' primaryExpression
    | getAttr
    ;

primaryExpression: '(' expression ')' | functionCall | atomExpression;

atomExpression: IntegerLiteral
              | DecimalLiteral
              | StringLiteral
              | BooleanLiteral
              | NilLiteral
              | Identifier
              | '{' argumentList? '}'
              ;

operator: '+' | '-' | '*' | '/' | '%' | '==' | '!=' | '<' | '>' | '<=' | '>=' | '&' | '|';

IntegerLiteral: Digit+;

DecimalLiteral: Digit+ '.' Digit+;

Apostrophe: '\'';
StringLiteral: '"' .*? '"' | Apostrophe .*? Apostrophe;

BooleanLiteral: 'true' | 'false';

NilLiteral: 'nil';

Comment: '//' ~[\r\n]* -> skip;
MultiLineComment: '/*' .*? '*/' -> skip;

Identifier: [a-zA-Z_] [a-zA-Z_0-9]*;

Digit: [0-9];

Whitespace: [ \t\n\r] -> skip;
