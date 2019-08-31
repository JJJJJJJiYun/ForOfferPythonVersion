# -*- encoding: utf-8 -*-


def is_stack_push_pop_order(push_order, pop_order):
    stack = []
    i = 0
    for num in pop_order:
        if len(stack) > 0 and stack[len(stack) - 1] == num:
            stack.pop()
        else:
            while i < len(push_order):
                stack.append(push_order[i])
                if push_order[i] == num:
                    i += 1
                    break
                i += 1
            if not stack.pop() == num:
                return False
    return True


if __name__ == '__main__':
    print is_stack_push_pop_order([1, 2, 3, 4, 5], [4, 3, 5, 1, 2])
