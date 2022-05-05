# Input  : a a b c
# Output : a -1 b b
#
# Input  : a a c
# Output : a -1 c

from queue import Queue


def first_non_repeating_char_in_stream(stream: str):
    queue = Queue()

    mem = {}

    result = []

    for i, value in enumerate(stream):
        queue.put(value)

        if value not in mem:
            mem[value] = 1
        else:
            mem[value] +=1

        while (not queue.empty()):
            if mem[queue.queue[0]] > 1:
                queue.get()
            else:
                result.append(queue.queue[0])
                break
        if queue.empty():
            result.append(-1)

    return result



if __name__ == '__main__':
    result = first_non_repeating_char_in_stream("aabc")
    print(result)
