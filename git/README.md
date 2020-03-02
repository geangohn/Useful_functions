# git_cmd_hints
Hints for Git, Docker and other

### 0. Cmd commands

- **pwd**   #present working directory
- **cd "new directory"**   #change directory
- **cp "from"  "to"**  #copy
- **cp -f "from"  "to"**  #Force to copy
- **mv "from"   "to"**  #move file
- **rm "filename"**   #remove file
- **ls**   #list of files in current directory


### 1.	Создать репозиторий
GitLab / GitHub -> New Repository (ставим галочку рядом с README.md)
```
>cd imaksimov/         # Папка в которой ты работаешь с репозиториями
>git clone “repo url”       # Скопировать репозиторий себе локально
>nano .gitignore       # открываем текстовые редактор, где пишем форматы файлов, которые не надо заливать в репозиторий
```
_Example_
.gitignore

*.csv
*.txt

```
>git add .gitignore   # Добавляем файл (новый/измененный) в очередь для заливания в репо
>git commit –m ‘added .gitignore’   # Оставляем комент к изменени.
>git push     # Заливаем в репозиторий
>pip freeze > requirements.txt   # Сохранить текущие версии библиотек, установленные на компе
```

### 2.	Добавить / изменить файл в репозитории
```
>cp –r “path_from/filename”  “repo_path”   # Копируем по адресу локально (-r для переноса папки, cp - copy)
>git add “filename”
>git commit “added file”
>git push
```

### 3.	Удалить файл
```
>git rm “filename”
>git commit “dropped file”
>git push
```

### 4.	Обновить репозиторий до последней версии (актуально, если работают в одном репозитории)
```
>git pull
```

### 5.	Скопировать файл внутри репозитория
```
>mv “path_from”  “path_to”   (mv – move)
>git add “filename”
>git commit –m ‘moved file’
```

### 6. Отменить какой-либо commit
Заходим в GitLab -> Repository -> Commits -> Copy commit SHA to clipboard
```
>git revert 'commit SHA'
>git push
```

### 7. Работа с ветками
```
>git status  # Посмотреть статус текущего репозитория

>git branch -a    # Вывести список всех веток
>git branch new_branch_name  # Создаьть новую ветку

>git checkout branch_name   # Переключиться на новую ветку

>git branch -d branchname   # удалить локальную ветку
>git push <remote_name> --delete <branch_name>  # Удалить удаленную ветку
```

### 8. Перенести вспе коммиты из одной ветки в другую
Заходимв ветку, *в которую* хотим перенести коммиты
```
> git checkout branch_name   # Переключиться на ветку *в которую* хотим перенести коммиты
>git rebase "ветка из которой переносим коммиты"
```




