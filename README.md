## Restaurant Project attempt #2
I decided we needed to just start again from scratch because not all of us contributed to the first project equally and thus didnt really learn much from it

### Notes (important please god read this)
- as long as we inform eachother before making changes and shit we should all be able to just push changes directly to the main branch even if we'd have to learn git
- when making commits please make the message as detailed as possible. you can make multiple local commits before pushing to github if you think this will be a problem
- `source ./.venv/bin/activate` will activate the virtual environment so that we're working with the same tools (python, rest, daraja)
  - `deactivate` will turn it off but you probably wont need to do this most of the time
- `python manage.py runserver` makes the site start running. `Ctrl+C` in terminal will turn it off
- this guy makes a bunch of useful videos on how to use git please watch them theyre not even long and he explains it better than i ever could
  - [Syncinc changes if someone else has already pushed their own to github](https://youtu.be/xN1-2p06Urc?si=jLOki01UYNA8-Cuv)
  - [Dealing with conflicts](https://youtu.be/DloR0BOGNU0?si=Sq-sqh5ZQSgTwKsq)
  - [Undoing a commit/push](https://youtu.be/GytsxgB4-HU?si=DAcWHI6h2iyov1aO) (i hope we never fucking need to do this)

### TO DO
1.
  - **FRONTEND** decide how the site will look and make changes to `base.html` to reflect that
  - **BACKEND** set up all the models and forms (BACKEND ONLY, use test page to set up simple form and see that they go to the django database)
2.
 - **FRONTEND** create and link all the forms on the backend to their respective pages (also make sure they actually work)
 - **BACKEND** make it possible to delete and modify data thats been added to the forms
3.
  - **FRONTEND** make `menupage.html` display both dishes original to the restaurant and submitted recipes
  - **BACKEND** mySQL :skull:
4.
  - **GENERAL** debugging :skull:
5.
  - **FRONTEND** display when users are logged in and add option to log out
  - **BACKEND** add mpesa functions through daraja (i also blacked out during this class i hope one of you is more familiar with it than me)
6.
  - **GENERAL** debugging again
7.
  - **OPTIONAL** make the blog page?

### Using git
#### _Downloading the project_
`git clone <link to project>.git` (you can copy this link directly from the colored dropdown in the code menu)
#### _Pushing changes to git_
```
git add . #adds all files to the commit
git commit -m "message" #commit message if its short
git commit #puts you into a menu that lets you add a more detailed commit
git push -u origin main #will send the changes youve made to github
```
Extra notes
- dont do both `git commit -m "message"` and the normal `git commit`
- check the page to make sure no ones done a push before you do your own
#### _what to do when someone has already done a push_
- go watch the 3 videos i linked above
```
git pull --rebase
```
and then you can do the push normally as long as nothing seems broken on your end
