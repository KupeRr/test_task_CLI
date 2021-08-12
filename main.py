import calculator.calculator    as module_calculate
import git_service.git_service  as module_git
import pokemon.pokemon          as module_pokemon

def __get_cmd_num():
    return int(input('=' * 100 + '\nChoose which module you are interested in [-1 -> exit]: '))

def __welcome_msg():
    print('Welcome to this service.\n' +
            'The functionality is represented by the following features:\n' +
            '1) Calculator\n2) Git-client\n3) Pokemon info')

def main():
    __welcome_msg()
    
    while True:
        cmd_num = __get_cmd_num()

        if cmd_num == 1:
            cmd = input('Enter the expression: ')
            module_calculate.calculate(cmd)

        elif cmd_num == 2:
            folder_name = input('Enter the name of the folder in which you want to load the project: ')
            git_link    = input('Enter the project URL: ')
            branch      = input('Enter the name of the branch: ')

            if input('Do you want to specify a local path to the folder?[y/n] ') == 'y':
                print('(Leave blank if you want to upload to the current folder)')
                path = input('Local path: ')
                module_git.load_project(folder_name, git_link, branch, local_path=path)
            else:
                print('(Leave blank if you want to upload to the current folder)')
                path = input('Path: ')
                module_git.load_project(folder_name, git_link, branch, path=path)

        elif cmd_num == 3:
            name = input('Enter the name of the selected pokemon: ')
            module_pokemon.get_pokemon_by_name(name)

        elif cmd_num != -1:
            print('Wrong number selected, try again')

        else:
            print('Shutdown...')
            break


if __name__ == '__main__':
    main()