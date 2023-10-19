---
title: PyTorch
date: 2023-04-12
фон: bg-[#ee4c2c]
теги:
  - ИИ
  - Python
категории:
  - Другое
intro: Это краткий справочный список шпаргалок для PyTorch. См. также [Сайт PyTorch](https://pytorch.org/)
---

## Импорты { .cols-1 }

### Общие сведения

```
import torch # корневой пакет
from torch.utils.data import Dataset, DataLoader # представление и загрузка наборов данных
```

### API нейронной сети

```
import torch.autograd as autograd # граф вычислений
from torch import Tensor # тензорный узел в графе вычислений
import torch.nn as nn # нейронные сети
import torch.nn.functional as F # слои, активации и многое другое
import torch.optim as optim # оптимизаторы, например, градиентный спуск, ADAM и т.д.
from torch.jit import script, trace # гибридный декоратор фронтенда и трассировки jit
```

### Torchscript и JIT

```
torch.jit.trace() # принимает ваш модуль или функцию и пример
                          # входные данные и отслеживает вычислительные шаги.
                          # с которыми сталкиваются данные при прохождении через модель

@script # декоратор, используемый для указания зависящего от данных
                          # поток управления в трассируемом коде
```

### ONNX

```
torch.onnx.export(model, dummy data, xxxx.proto) # экспорт ONNX-формата
                                                       # модель, используя обученную модель, фиктивные
                                                       # данных и желаемого имени файла

model = onnx.load("alexnet.proto") # загрузка ONNX-модели
onnx.checker.check_model(model) # проверка того, что модель
                                                       # IR хорошо сформирована

onnx.helper.printable_graph(model.graph) # распечатать человекочитаемое
                                                       # представление графа
```

### Vision


```
from torchvision import datasets, models, transforms # наборы данных по зрению,
                                                         # архитектуры &
                                                         # transforms

import torchvision.transforms as transforms # композитные преобразования
```

### Распределенное обучение

```
import torch.distributed as dist # распределенное взаимодействие
from torch.multiprocessing import Process # процессы с разделением памяти
```

## Тензоры { .cols-1 }

### Создание

```
x = torch.randn(*size) # тензор с независимыми записями N(0,1)
x = torch.[ones|zeros](*size) # тензор со всеми 1 [или 0]
x = torch.tensor(L) # создание тензора из [вложенного] списка или ndarray L
y = x.clone() # клон x
with torch.no_grad():               # обертка кода, которая не позволяет автограду отслеживать историю тензора
requires_grad=True # arg, при установке значения True, отслеживает историю вычислений
                                    # история для будущих вычислений производных
```

### Размерность

```
x.size() # возвращает кортежеподобный объект размерности
x = torch.cat(tensor_seq, dim=0) # конкатенирует тензоры по dim
y = x.view(a,b,...) # переформировывает x в размер (a,b,...)
y = x.view(-1,a) # переформирование x в размер (b,a) для некоторого b
y = x.transpose(a,b) # поменять местами размеры a и b
y = x.permute(*dims) # перестановка размеров
y = x.unsqueeze(dim) # тензор с добавленной осью
y = x.unsqueeze(dim=2) # тензор (a,b,c) -> тензор (a,b,1,c)
y = x.squeeze() # удаляет все размерности размера 1 (a,1,b,1) -> (a,b)
y = x.squeeze(dim=1) # удаляет заданную размерность размера 1 (a,1,b,1) -> (a,b,1)
```

### Алгебра

```
ret = A.mm(B) # матричное умножение
ret = A.mv(x) # матрично-векторное умножение
x = x.t() # транспонирование матрицы
```

### Использование GPU

```
torch.cuda.is_available # проверка наличия cuda
x = x.cuda() # перемещение данных x с
                                                            # CPU на GPU и возвращает новый объект

x = x.cpu() # перемещение данных x с GPU на CPU
                                                            # и вернуть новый объект

if not args.disable_cuda and torch.cuda.is_available():     # код, не зависящий от устройства
    args.device = torch.device('cuda') # и модульность
else:                                                       #
    args.device = torch.device('cpu') #

net.to(device) # рекурсивно преобразует их
                                                            # параметры и буферы в
                                                            # тензоры, специфичные для конкретного устройства

x = x.to(device) # копирование тензоров на устройство
                                                            # (gpu, cpu)
```

### Глубокое обучение

```
nn.Linear(m,n) # полностью связанный слой из
                                              # от m до n единиц

nn.ConvXd(m,n,s) # X-мерный сверточный слой от
                                              # от m до n каналов, где X⍷{1,2,3}
                                              # и размер ядра равен s

nn.MaxPoolXd(s) # X-мерный пулирующий слой
                                              # (обозначения как выше)

nn.BatchNormXd # слой пакетной нормы
nn.RNN/LSTM/GRU # рекуррентные слои
nn.Dropout(p=0.5, inplace=False) # слой отсева для входных данных любой размерности
nn.Dropout2d(p=0.5, inplace=False) # двумерное канальное выпадение
nn.Embedding(num_embeddings, embedding_dim) # (тензорное) отображение от
                                              # индексов к векторам вкраплений
```

### Функции потерь

```
nn.X # где X - L1Loss, MSELoss, CrossEntropyLoss
                                      # CTCLoss, NLLLoss, PoissonNLLLoss,
                                      # KLDivLoss, BCELoss, BCEWithLogitsLoss,
                                      # MarginRankingLoss, HingeEmbeddingLoss,
                                      # MultiLabelMarginLoss, SmoothL1Loss,
                                      # SoftMarginLoss, MultiLabelSoftMarginLoss,
                                      # CosineEmbeddingLoss, MultiMarginLoss,
                                      # или TripletMarginLoss
```

### Функции активации

```
nn.X # # где X - ReLU, ReLU6, ELU, SELU, PReLU, LeakyReLU,
                                      # RReLu, CELU, GELU, Threshold, Hardshrink, HardTanh,
                                      # Sigmoid, LogSigmoid, Softplus, SoftShrink,
                                      # Softsign, Tanh, TanhShrink, Softmin, Softmax,
                                      # Softmax2d, LogSoftmax или AdaptiveSoftmaxWithLoss
```

### Оптимизаторы

```
opt = optim.x(model.parameters(), ...)      # создать оптимизатор
opt.step() # обновление весов
optim.X # где X - SGD, Adadelta, Adagrad, Adam,
                                            # AdamW, SparseAdam, Adamax, ASGD,
                                            # LBFGS, RMSprop или Rprop
```

### Планирование скорости обучения

```
scheduler = optim.X(optimizer,...) # создание планировщика lr
scheduler.step() # обновление lr после обновления весов оптимизатором
optim.lr_scheduler.X # где X - LambdaLR, MultiplicativeLR,
                                        # StepLR, MultiStepLR, ExponentialLR,
                                        # CosineAnnealingLR, ReduceLROnPlateau, CyclicLR,
                                        # OneCycleLR, CosineAnnealingWarmRestarts,
```

## Утилиты данных { .cols-1 }

### Наборы данных

```
Dataset # абстрактный класс, представляющий набор данных
TensorDataset # маркированный набор данных в виде тензоров
Concat Dataset # конкатенация наборов данных
```

### Dataloaders и DataSamplers

```
DataLoader(dataset, batch_size=1, ...) # загрузка пакетов данных, не зависящих
                                            # от структуры отдельных точек данных

sampler.Sampler(dataset,...) # абстрактный класс, рассматривающий
                                            # способами выборки из набора данных

sampler.XSampler, где ...                  # Sequential, Random, SubsetRandom,
                                            # WeightedRandom, Batch, Distributed
```