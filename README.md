# INPROS

livre du cours **INPROS** utilisant jupyter-book

# version html

- [https://mbuffat.github.io/INPROS/intro.html](https://mbuffat.github.io/INPROS/intro.html)

## création du livre

```
cd ..

jupyter-book build INPROS/
```
crétion d'une version html statique dans **INPROS/_build/html/**

- [version statique html](_build/html/index.html)

## gestion sous git

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd  INPROS
git remote add origin https://forge.univ-lyon1.fr/MARC.BUFFAT/inpros.git
git branch -M main
git push -uf origin main
```
puis
```
git commit -a -m "texte"
git push
```
ou sous github  (remote github sous p2chpd-visu2)

```
git push github
```
## syntaxe markdown

### notation markdown jupyter-book  
```{admonition} Title
text
```
```{note}
text
```
```{warning} text
some more text...
```
```{tip} text
some more text...
```
```{caution} text
some more text...
```
```{attention} text
some more text...
```
```{danger} text
some more text...
```
```{error} text
some more text...
```
```{hint} text
some more text...
```
```{important} text
some more text...
```

### référence
-  [Myst markdown syntaxe](https://jupyterbook.org/reference/cheatsheet.html)


## Authors and acknowledgment
Marc BUFFAT, dot mécanique, Ubiversité Lyon 1

## License
Projet sous licence libre, mais sans garantie

## Project status
