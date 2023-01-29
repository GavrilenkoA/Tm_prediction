# Tm_prediction


Проект посвящен предсказанию температуры плавления белков на основе первичной последовательности белков. 

1. **Данные**
- data/merged_data.csv

Данные использовались из эксперимента по измерению почти 40000 тысяч белков модельных организмов. [http://meltomeatlas.proteomics.wzw.tum.de:5003/](http://meltomeatlas.proteomics.wzw.tum.de:5003/) 

2. **Процессинг данных.**
- process_data/*process_data.ipynb*

Предварительно данные последовательностей были обработаны. Поскольку для кодирования признаков использовалась языковая модель ESM на основе трансформера, учитывающая контекст длины не более чем 1020 букв, последовательности длиннее чем 1020 были исключены. 

- process_data/filter_homologs*.ipynb*

Для избегания избыточности однотипных данных (в датасете существуют  гомологичные последовательности - то есть что-то похожее на тест могло встретиться и в трейне), была привидена кластеризация по  группам в соотвестии температурой плавления (Thermophilic, Mesophilic, Hyperthermophilic) c помощью [https://sites.google.com/view/cd-hit](https://github.com/weizhongli/cdhit-web-server)   

В конечном счете были выбраны наиболее репрезентативные последовательности из каждого кластера. 

3. **Кодирование последовательностей**

data/esm/overall_emb.zip (лежат на кагле) 

Для всех последовательностей из датасета были получены эмбединги с помощью предобученной языковой модели для белков ESM. https://github.com/facebookresearch/esm 

Эмбединги размерности 1280 для каждой последовательности.

 4. **Обучение ML моделей.** 

[!https://www.kaggle.com/code/alexandrgavrilenko/experiment-full-embed]

Использовались  все модели градиентого бустинга и также нейросеть на Табличных данных TabNet.

Лучшие результаты усреднялись от моделй lightGBM и TabNet усреднялись. 

Показаны лучшие метрики на тех же данных что и в статье  [https://www.mdpi.com/1422-0067/23/18/10798](https://www.mdpi.com/1422-0067/23/18/10798), где явно кодировались физико-химические характеристики белков, показывает что эмбединги работают лучше. 
