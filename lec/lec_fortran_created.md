1. Имеем Железо(Аппаратное обеспечение, Hardware), которое предоставляет даже такие древние возможности, которые 
были в 80х(Речь про Интел и АМД, Qualcom(Snapdragon, Samsung(exynos), Apple(A series) и прочие такого наследия не 
имеют) . Железо стало быстрее, научилось делать некоторые вещи одновременно, но оно, тем не менее, все так же 
Использует 1010101 внутри себя и общаться напрямую, т.е. создавать файлы, которые без обработки будут готовы
к исполнению на Процессоре можно только из 10101, таков понятный ему алфавит. Не особо удобно, точнее может для 
кого - то и прикольно
было в то время поугарать над таким, но круг ценителей был не столь велик. Академическая среда. А вот уже что - то 
научное попрогать не выйдет. 

Придумали создать язык для ученых(стояли сильно задачи по проектированию, а затем
и по моделированию оружие по заданным условиям, для задач поиска оптимальных решений), Времена мечтателей космоса. 
В 57ом создали фортран и полетел первый спутник. Контекст считаю важным в силу того, что прогресс двигается 
деньгами, у кого больше тот больше влияния и оказывает. Фортран давал абстракции, которые необходимы ученым и 
инженерам (шутка про инженера и справочник объемов красных шаров). Удобные матрицы, интуитивность для инженера. 
Маткад своего времени, но так вышло, что он так долго был один такой под него написали вагон всего нужного
для очень многих сфера науки и техники. На работе нужен так или иначе если заниматься делом. Инструмент готовили
для расчетов, компьютеры были шкафами, помещениями... (по иронии сегодня они тоже шкафы и помещения и еще пару 
десятков ролей). Потом пришла необходимость делать ПО под разные архитектуры... )) архитектуры меняли друг друга
не как сейчас. IBM тогда делала свои процессоры и частенько свежий комп оказывался не в состоянии пускать
exe - шники того времени. Сейчас такое дико, а тогда реалии и решили в одной из лабораторий сделать язык С...
Язык писался под вдохновением от ОС Unix  и для нее и потому можно проследить некую похожесть.
Язык для написания операционных систем, а не для инженеров. Потому они хоть и выглядят одинаковой мишурой, но
занимают очень разные ниши. 

2. Появилась возможность писать не используя перфокарты(типичный способ ввода вещей типа 10101) и не используя
термины(абстракции) адрес памяти, регистр(ячейка в процессоре, куда можно сохранить 10101 определенной длины, 
прослеживается корреляция с битностью ОС). Например 
  -Помести в регистр А число 5
  -Помести в регистр B число 3
  -Произведи сложение //В этом месте процессора пинают и говорят: складывай два целых числа
Все его действия пронумерованы. Ему говорят номер  и он знает, что этот номер означает.( Как почтальон
знает что если телеграммой передали номер  51 то это открытка с 8марта и он именно ее понесет адресату в срочном 
порядке. ) Он знает, что при команде номер 51 (Сложение целых чисел) необходимо прочесть значение регистра А, 
регистра В , сложить прочитанное и записать в регистр А. Программировать в таких терминах неудобно.
Код на фортране куда приятнее, можно не особо понимая языка или не во всех строчках разобравшись
понять что тут происходит и может даже исправить что - то. Двигалось это, напомню, необходимостью переносить ПО, а 
все потому что разработка ПО это тот еще (попил бабла) источник непредсказуемости в плане сроков и финансов, 
особенно в то время. Не только у нас делали абы как, а иногда и не делали. В итоге ПО дорого стоит, переписывание
тоже, захотелось стоб ехе - шники от предыдущих поколений можно было запускать на новом железе и получать 
старые добрые правильные результаты на еще более быстром железе ничего не переписав.

В случае с железом вы работает с 1010101010 и должны знать какие комбинации что значат, для ваших задач не идет

В случае с асемблером вы работаете с регистрами(подобие переменных, но скорее ящики на n - единиц и нулей), процедурами и их вызовами(аргументов у функций там нет и поэтому все сначала запихивают в спец шкаф, а потом
уже в процедуре достают.). каждая команда ассемблера однозначно соответствует какому - то уникальному набору 1010101
Хотя в макроассемблере одна команда может скрывать другие, но это уже не надо...

В случае с фортраном вы получаете удобные матрицы и кучу готовых библиотек для ученых

В слуае с С вы имеете массу софта системного уровня и для работы с железом. Иногда на этом делают вычисления. Тоже
нужно знать, может пригодиться, используется. С++ уже в более обзорном вариант, достаточно представлять классы
и уметь хоть как - то свою прогу на объекты поделить.