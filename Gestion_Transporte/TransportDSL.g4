grammar TransportDSL;

prog: stat+ ;

stat
    : loadStmt
    | filterStmt
    | aggregateStmt
    | printStmt
    ;

loadStmt: 'load' STRING ';' ;
filterStmt: 'filter' 'column' STRING compOp value ('AND' 'column' STRING compOp value)* ';' ;
aggregateStmt: 'aggregate' aggFunc 'column' STRING ';' ;
printStmt: 'print' ';' ;

aggFunc: 'count' | 'sum' | 'average' ;

compOp: '>=' | '<=' | '>' | '<' | '==' | '!=' ;

value: STRING | NUMBER ;

STRING: '"' (~["\r\n])* '"' ;
NUMBER: [0-9]+ ('.' [0-9]+)? ;

WS: [ \t\r\n]+ -> skip ;
