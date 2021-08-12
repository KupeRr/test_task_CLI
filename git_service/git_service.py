import os

import click
import git

#def __fetch_repo(folder_name, file_path, git_link, branch):
#    local_repo_directory = os.path.join(file_path, folder_name)
#    repo = git.Repo(local_repo_directory)
#
#    for remote in repo.remotes:
#        remote.fetch()


def __get_repo(folder_name, file_path, git_link, branch):
    """
    Clones a project or downloads the latest version.
    """

    local_repo_directory = os.path.join(file_path, folder_name)

    if os.path.exists(local_repo_directory):
        print(f'Pulling changes from {branch} branch...')
        repo    = git.Repo(local_repo_directory)
        origin  = repo.remotes.origin
        origin.pull(branch)
    else:
        print(f'Cloning project from {git_link} from {branch} branch...')
        git.Repo.clone_from(git_link, local_repo_directory, branch=branch)

@click.command()
@click.argument('folder-name')
@click.option('--path', '-p', 
                help='Path to the folder of the repository.')
@click.option('--local-path', '-lp', 
                help='Path to the repository folder from the current folder.')
@click.option('--git-link', '-gl', 
                help='HTTPS path to github repository.')
@click.option('--branch', '-b', 
                help='Necessary branch name of the repository')
@click.option('--fetch', '-f', is_flag=True,
                help='Mode, if you want use FETCH instead of PULL')
def __main(folder_name, path, local_path, git_link, branch, fetch):
    """
    This module allows you to work with repositories from GitHub. 
    It allows you to select the desired project, create a copy of it if it is not yet uploaded. 
    In case you already have a copy of the project, then it will upload the latest version of the project. 
    
    By default, without parameters, it will load the demo project, in the folder from which it is called.
    """

    load_project(folder_name, git_link, branch, path, local_path, fetch)
    
    
def load_project(folder_name, git_link, branch, path        = '', 
                                                local_path  = '', 
                                                fetch       = ''):

    if git_link == '' or not git_link:  git_link = 'https://github.com/KupeRr/test.git'
    if branch == '' or not branch:      branch   = 'main'

    if local_path != '' and local_path: path = os.path.join(os.getcwd(), local_path)
    elif path == '' or not path: path = os.getcwd()

    if folder_name == '': 
        print('Error. The file name is missing.')
        return

    #if fetch: __fetch_repo(folder_name, path, git_link, branch)  
    #else:     __get_repo(folder_name, path, git_link, branch)
    
    __get_repo(folder_name, path, git_link, branch)


if __name__ == "__main__":
    __main()