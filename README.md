
# Abordagens para melhorar o desempenho no processo de execução do códigos 

Dependendo do motivo de cada programa, o tempo de execução não é um ponto relevante para a terefa exercida o processo do inicio ao fim não traz mudança na conclusão do software.   
Programas especificos necessitam de maior volume de processo para um resultado exato, são os casos de utilização de api's e calculos de grande volumes cuja diferenças podem disponibilizar recursos simultaneamente.

No contexto de dispor mais agilidade ao funcionamento as linguagens de programação oferençem meios para ganhos de tempo essencialmente a linguagem python aqui implementada há o termono chamado de [gil](https://www.machinelearningplus.com/python/python-global-interpreter-lock-gil/) que impede a liberdade de exercer o controle total no entanto existem outros meio de evita-lo (não utilizei nesses prototipos) mas utilizando recusos building na versão atual é possivel minimzar e obter ganhos.




“O número de transistores em um circuito integrado irá dobrar a cada 18 meses.”   
([Lei de Moore](https://mittechreview.com.br/nos-nao-estamos-preparados-para-o-fim-da-lei-de-moore/))
 
 
 
 ## Tipos  de concorrência:  
Programação paralela e assíncrona.

Programação assíncrona:  
múltiplas instruções sequenciais
ao mesmo tempo.         
([ programação assíncrona](https://developer.mozilla.org/pt-BR/docs/Learn/JavaScript/Asynchronous/Concepts)
).

Programação paralela:   
dividi em pequenas sub-tarefas executálas em múltiplos cores de forma simultânea.  
([programação paralela](https://pt.wikipedia.org/wiki/Computa%C3%A7%C3%A3o_paralela
))

Global Interpreter Lock  
 Recurso de bloqueio  previne  múltiplas threads nativas executem em um código ao mesmo tempo.
necessário para manter a thread de execução segura(gerenciamento interno de memória do
interpretador Python não é thread-safe.)  
([GIL](https://www.machinelearningplus.com/python/python-global-interpreter-lock-gil/))



 ![GitHub](https://img.shields.io/badge/python-3.9-blue) ![GitHub](https://img.shields.io/badge/licence-MIT-GREE) 
