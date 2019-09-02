import sys
import os

def push():
  print 'Enter branch name'
  branch = raw_input()
  os.system('git push origin '+branch)

def pull():
  print 'Enter branch name'
  branch = raw_input()
  os.system('git pull origin '+branch)

def checkout():
  print 'Enter branch name to be checkout'
  checkout = raw_input()
  os.system('git checkout '+checkout)

def status():
  os.system('git status')

def new_branch():
  print 'Enter branch name'
  new_branch = raw_input()
  os.system('git checkout -b '+new_branch)

def add_files():
  os.system('git add .')

def new_commit():
  print 'Enter commit message'
  message = raw_input()
  os.system('git commit -m '+message)

def rename_branch():
  print 'Enter new branch name'
  new = raw_input()
  os.system('git branch -m '+new)

def delete_branch():
  print 'Please make sure you are not on the same branch which needs to be deleted'
  print 'Enter branch to be deleted'
  delete = raw_input()
  os.system('git branch -D '+delete)

def list_branches():
  os.system('git branch')

def exit():
  sys.exit() 

while True:
  print '1 Push a branch'
  print '2 Pull a branch'
  print '3 Checkout to a branch'
  print '4 Status'
  print '5 Create a new branch and checkout to it'
  print '6 Add all files'
  print '7 Add a single line commit in double quotes'
  print '8 Rename a branch'
  print '9 Delete a branch'
  print '10 List all branches and see the current branch'
  print '11 Exit'
  print 'Enter your choice'
  cmd = raw_input()

  if cmd == '1':
    push()
  elif cmd == '2':
    pull()
  elif cmd == '3':
    checkout()
  elif cmd == '4':
   status()
  elif cmd == '5':
    new_branch()
  elif cmd == '6':
    add_files()
  elif cmd == '7':
    new_commit()
  elif cmd == '8':
    rename_branch()
  elif cmd == '9':
    delete_branch()
  elif cmd == '10':
    list_branches()
  elif cmd == '11':
    exit()
  else:
    print 'Something Went Wrong!'
