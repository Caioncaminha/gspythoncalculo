A GS é um projeto interdisciplinar, vou colocar o contexto das matérias "Python" e "Cálculo"


Python:
Case:
O trabalho está passando por uma transformação radical, impulsionada pela inteligência artificial, robótica e automação. De acordo com a ONU e a OIT, até 2030, milhões de empregos podem ser extintos, mas outros tantos surgirão, exigindo uma requalificação constante dos profissionais. Esta mudança requer o desenvolvimento de habilidades humanas fundamentais como empatia, criatividade e colaboração, além de pensamento crítico
Esta transformação representa uma grande oportunidade para reimaginar o trabalho e criar soluções que tornem o mundo mais inclusivo, ético e sustentável. Quando conectamos tecnologia, propósito e pessoas, abrimos caminho para transformar vidas e o próprio significado do trabalho
O trabalho:
Nesse trabalho, vocês criarão funções para fazer análise estatística de que fatores influenciam a evolução do mercado de trabalho.
A primeira fase do trabalho será localizar e importar para o python dados relevantes para a comparação de países. Vocês deverão utilizar dados descrevendo algumas variáveis de interesse (podem ser essas que eu estou mostrando, podem ser outras)
https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population
https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)_per_capita 
https://en.wikipedia.org/wiki/Retirement_age#Retirement_age_by_country_and_region 
https://en.wikipedia.org/wiki/List_of_countries_by_labour_force 
https://en.wikipedia.org/wiki/List_of_countries_by_sector_composition_of_the_labor_force 
https://www.gapminder.org/tools/#$ui$chart$opacitySelectDim:0;;&model$markers$bubble$encoding$size$data$constant=_default;&scale$domain:null&type:null&zoomed:null&extent@:0&:0;;;&y$data$concept=gini&space@=geo&=time;;&scale$domain:null&zoomed:null&type:null;;&x$data$concept=time&space@=time;;&scale$domain:null&zoomed:null&type:null;;&trail$data$filter$markers$chn=1800&swe=1800&vnm=1800&che=1800;;;;;;;;&chart-type=bubbles&url=v2 
O site gapminder tem uma série de dados que podem ser úteis. No exemplo acima, ele está mostrando a evolução do GINI através do tempo – O GINI é um indice de desigualdade econômica, mas você pode explorar diversos outros indices
Depois de explorar os dados no site, você pode baixar aqui: https://www.gapminder.org/data/ 
Os dados devem estar disponíveis no python utilizando-se:
Dicionários codificados na mão OU
Arquivos CSV, e funções auxiliares para a carga desses dados
Isso não foi apresentado em sala, mas é bem fácil. Venha falar comigo nos horários indicados na primeira folha, se tiver alguma dificuldade.
(mais dificil, bonus) acessando diretamente uma API disponivel publicamente
Vocês devem utilizar
Pelo menos 5 tipos de dados diferentes (exemplo: população, PIB – em inglês GDP, porcentagem da força de trabalho em agricultura)
Dados de pelo menos 20 países diferentes
Não há problema se algum dado não existir para algum país. Dados reais são assim mesmo!
Para apresentar os dados, o código de vocês deve ter as seguintes funções:
Apresenta dado – Recebe um nome de um dado (como o PIB, ou a porcentagem da população trabalhando em agricultura) e retorna aquele dado para todos os países
Apresenta país – Recebe um nome de um país, e retorna todos os dados disponíveis para aquele país, em formato de um dicionário
Para trabalhar os dados, o código de vocês deve conter as seguintes funções estatísticas
Calcula média de dado: Recebe um nome de um dado (como o PIB, ou a porcentagem da população trabalhando em agricultura) retorna a média dos valores do dado.
Calcula variância de dado: o mesmo para a variância
O que é mesmo variância?
https://pt.wikipedia.org/wiki/Vari%C3%A2ncia
https://brasilescola.uol.com.br/matematica/medidas-dispersao-variancia-desvio-padrao.htm 
Calcula média ponderada de dado: Recebe um nome de um dado, e produz uma média ponderada (pelo número de habitantes, ou pelo PIB, ou pelo tamanho do país em área, ou por outra variável que você queira)
Mais uma função estatística à sua escolha. Pode fazer o cálculo da correlação entre duas variáveis (https://pt.wikipedia.org/wiki/Correla%C3%A7%C3%A3o  ) , ou o cálculo da mediana (https://pt.wikipedia.org/wiki/Mediana_(estat%C3%ADstica) ), ou uma média ‘filtrada’, só de países grandes, ou outra estatística que ache interessante
Se qualquer uma dessas funcionalidades não estiver clara para você, lembre-se que podemos conversar presencialmente, ou via Teams. 
Via de regra, conversas ao vivo (seja presencialmente, seja via Teams) permitem um esclarecimento melhor das suas dúvidas do que o envio de mensagens
Critérios de avaliação:
Os dados devem estar representados em arquivos CSV separados, ou em dicionários bem organizados. Apresentar em listas não é considerado válido. Deve haver dados na quantidade pedida, ou mais (pelo menos 5 variáveis, pelo menos 20 países) – 20 pontos. Em ambos os casos (CSV ou dicionários) é necessário apresentar código de boa qualidade, caso contrário, poderá haver descontos.
Lembre-se também de dizer de onde vieram os dados! Não vou exigir uma citação formal, mas coloque pelo menos um link – a ausência dessa informação poderá ocasionar descontos nesse critério
As funções de exibição valem 20 pontos, incluindo a funcionalidade e qualidade de código
Cada uma das funções estatísticas vale 15 pontos, incluindo a funcionalidade e a qualidade de código – quando possivel, use o fato de que algumas funções podem chamar outras, e reduza ao máximo a repetição de código

Cálculo:

Tema: Aprendizado contínuo e requalificação – a curva do conheci-
mento no futuro do trabalho
Contexto: O avanço da tecnologia e da inteligência artificial exige que os profissionais se rein-
ventem constantemente. A requalificação e o aprendizado contínuo tornaram-se competências
essenciais. Assim como o crescimento de um sistema físico ou biológico, o desenvolvimento do
conhecimento humano pode ser representado por funções matemáticas — mostrando como
aprendemos rapidamente no início e depois atingimos um nível de estabilização.
Modelar essa curva matematicamente nos ajuda a compreender como o tempo e o esforço
de estudo impactam o aprendizado, e como podemos planejar estratégias de capacitação mais
eficientes para o futuro do trabalho.
Objetivos de Desenvolvimento Sustentável (ODS):
Deve-se relacionar as análises com os seguintes objetivos definidos pela ONU:
• ODS 4 – Educação de qualidade;
• ODS 8 – Trabalho decente e crescimento econômico.
Essas conexões devem aparecer de forma explícita no texto do relatório, demonstrando como
o aprendizado contínuo e a requalificação contribuem para um futuro do trabalho mais justo
e inovador.
Desafio
Crie uma função que modele o crescimento do conhecimento ao longo do tempo de estudo e
explore:
• Limites – para representar o conhecimento máximo possível;
• Derivadas – para medir a velocidade de aprendizado;
• Integrais – para estimar o total de conhecimento acumulado.
Represente graficamente a curva de aprendizagem e interprete os resultados em relação à
importância do aprendizado contínuo e da requalificação.
1
Etapas de desenvolvimento
1. Defina as variáveis:
• t: tempo de estudo (em meses ou semanas);
• K(t): nível de conhecimento adquirido.
2. Escolha uma função coerente:
K(t) = 100(1 − e^−0.2t) ou K(t) = 100/1 + e^−0.3(t−10)
3. Aplique os conceitos:
• Calcule o limite lim de t→∞ K(t);
• Derive K′(t) para identificar o ritmo de aprendizado;
• Integre K(t) para estimar o conhecimento total acumulado.
4. Construa os gráficos de K(t) e K′(t), destacando:
• Fase de aprendizado rápido;
• Fase de estabilização;
• Ponto de inflexão.
5. Interprete os resultados:
• Quando o aprendizado é mais intenso?
• O que o limite representa?
• Como a requalificação contínua mantém o crescimento?
6. (Opcional): use Python para automatizar os cálculos e gráficos.
Entrega esperada
O trabalho deve ser obrigatoriamente digitado e entregue em formato digital (PDF),
não sendo aceitas fotos de caderno, manuscritos ou arquivos escaneados. O arquivo
deve conter o nome completo e o número de matrícula (RM) de todos os integrantes
no cabeçalho, no início do documento.
O relatório deverá seguir o formato de artigo científico curto, com 3 a 5 páginas digi-
tadas, redigido de forma clara, coesa e organizada, contendo:
• Contexto e definição das funções utilizadas;
• Identificação do domínio, imagem e comportamento das funções;
• Gráficos bem apresentados e analisados;
• Interpretação dos resultados e reflexão crítica sobre o tema.
2
Critérios de Avaliação
A avaliação considerará não apenas a construção das funções, mas também a clareza da
explicação, a coerência entre o modelo e o contexto, e a capacidade de análise crítica. Cada
item abaixo corresponde a 25% da nota final.
Dimensão Avaliada Descrição do que será conside-
rado
Peso
1. Modelagem Matemática e Con-
textualização
Escolha adequada das funções; de-
finição clara das variáveis; coerên-
cia entre o modelo e o contexto do
aprendizado e requalificação.
25%
2. Análise e Interpretação Matemá-
tica
Correção na identificação de domí-
nio, imagem e comportamento da
função; interpretação coerente dos
resultados obtidos.
25%
3. Representação Gráfica e Organi-
zação
Gráficos bem construídos, legíveis e
identificados; uso correto de eixos
e legendas; relação coerente entre o
gráfico e o fenômeno descrito.
25%
4. Reflexão Crítica e Conexão com
os ODS
Capacidade de relacionar o modelo
matemático aos ODS 4 e 8; argu-
mentação fundamentada e escrita de
forma clara e organizada.
25%
Observação: a nota poderá ser reduzida caso o trabalho apresente erros conceituais, ausência
de itens obrigatórios, falta de identificação dos integrantes ou não observância das orientações
de entrega.
Orientações Finais
• Todos os entregáveis deverão conter o nome completo e o número de matrícula (RM)
de todos os integrantes;
• Não envie links externos: poste todos os entregáveis diretamente no Portal/Teams, nos
formatos exigidos;
• Após o prazo de entrega, o sistema não aceitará envios posteriores;