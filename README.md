## Результат вимірювання

| Розмір | Тип масиву              | Сортування злиттям | Сортування вставками | Timsort   |
|--------|-------------------------|--------------------|----------------------|-----------|
| 1000   | Випадковий              | 0.000933           | 0.011146             | 0.000079  |
| 1000   | Майже відсортований     | 0.000884           | 0.002683             | 0.000052  |
| 1000   | Зворотно відсортований  | 0.000833           | 0.021484             | 0.000007  |
| 2000   | Випадковий              | 0.002046           | 0.048955             | 0.000164  |
| 2000   | Майже відсортований     | 0.002073           | 0.011028             | 0.000103  |
| 2000   | Зворотно відсортований  | 0.001613           | 0.091903             | 0.000019  |
| 5000   | Випадковий              | 0.005815           | 0.310022             | 0.000439  |
| 5000   | Майже відсортований     | 0.005467           | 0.072285             | 0.000261  |
| 5000   | Зворотно відсортований  | 0.004693           | 0.599753             | 0.000027  |
| 10000  | Випадковий              | 0.012408           | 1.243278             | 0.000941  |
| 10000  | Майже відсортований     | 0.011498           | 0.278195             | 0.000498  |
| 10000  | Зворотно відсортований  | 0.010186           | 2.458458             | 0.000056  |

## Аналіз

Результати вимірювань часу виконання показують, що:

### Сортування вставками:
- Найповільніший алгоритм для великих масивів, особливо на випадкових і зворотно відсортованих масивах.
- Ефективний для майже відсортованих масивів.

### Сортування злиттям:
- Має стабільну швидкість на всіх типах масивів.
- Ефективніший ніж сортування вставками на великих наборах даних.

### Timsort:
- Найефективніший алгоритм, особливо на великих наборах даних.
- Поєднує ефективність сортування злиттям і сортування вставками, використовуючи їх переваги.

## Висновки

Поєднання сортування злиттям і сортування вставками в Timsort робить його значно ефективнішим для реальних задач. Timsort використовує сортування вставками для невеликих масивів, де він ефективний, і сортування злиттям для більших частин масиву, що забезпечує загальну високу продуктивність. Саме з цієї причини програмісти зазвичай використовують вбудовані алгоритми Python, такі як `sorted`, замість написання власних реалізацій.
