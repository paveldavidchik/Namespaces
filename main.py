
from Namespaces import Namespace


def main():
    command_list = []
    n = int(input())
    for _ in range(n):
        command_list.append(input().split())
    namespace = Namespace('global')
    for command, space, val in command_list:
        if command == 'create':
            namespace.create_namespace(space, val)
        elif command == 'add':
            namespace.add_var(space, val)
        elif command == 'get':
            print(namespace.get_namespace(space, val))
        else:
            raise ValueError


if __name__ == '__main__':
    main()
