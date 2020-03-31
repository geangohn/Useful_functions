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

CTR = sum(clicks) / sum(views)
![formula](https://render.githubusercontent.com/render/math?math=^{i \pi} = -1)

CTR_weighted = sum(sqrt(views) * clicks / views) / sum(sqrt(views))

####
