## 1. Классические А/В тесты
### 1.1 Параметрические

*t-test*

n_min = sigma^2 * (z_alpha + z_beta)^2 / effect^2

*ANOVA*

### 1.2 Непараметричкеские 

*![Хи-квадрат](http://latex.codecogs.com/svg.latex?%5Cchi%5E2)*

*Fisher's exact test*

*U-критерий (критерий Манно-Уитни)*

## 2. Ускорение А/В тестов
### 1.1 Перевзвешивание (для относительных метрик)
Позволяет более активным пользователям, которые совергают больше действий, иметь более высокий вес в метирке --> метрика более чувствительна к изменениям, так как активные польщзователи быстрее меняют свое поведение

![formula-1](https://latex.codecogs.com/gif.latex?CTR%20%3D%20%5Cfrac%7B%5Csum%20%7Bclicks%7D%7D%20%7B%5Csum%20views%7D)
![formula-2](https://latex.codecogs.com/gif.latex?CTR_%7Bweighted%7D%20%3D%20%5Cfrac%7B%5Csum%20%5Csqrt%20views%20*%20%5Cfrac%7B%7Bclicks%7D%7D%20%7Bviews%7D%7D%7B%5Csum%20%5Csqrt%20views%7D)

Это пример перевзвешивания по кол-ву просмотров. Можно брать другие веса для перевзвешивания

#### 1.2 Линеаризация
Подходит для относительных метрик. В случае применения совместно с перевзвешиванием, сначала считаем *K*, а потом перевзвешиваем
![formula-4](https://latex.codecogs.com/gif.latex?CTR%20%3D%20%5Cfrac%7B%5Csum%20%7Bclicks%7D%7D%20%7B%5Csum%20views%7D)
![formula-3](https://latex.codecogs.com/gif.latex?%5Csum%20%7Bclicks%7D%20-%20K*%20%7Bviews%7D),
где *K* - CTR на контроле
