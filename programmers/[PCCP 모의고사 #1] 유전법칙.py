# https://school.programmers.co.kr/learn/courses/15008/lessons/121685

def get_child_gene(parent_gene, num) :
    if parent_gene == 'RR' :
        return 'RR'
    elif parent_gene == 'Rr' :
        if num == 0 :
            return 'RR'
        elif num > 0 and num < 3 :
            return 'Rr'
        else :
            return 'rr'
    else :
        return 'rr'

def get_parents(gen, order) :
    parent_gen = gen - 1
    parent_order = order // 4
    rest = order % 4
    return parent_gen, parent_order, rest

def solution(queries):
    answer = []
    for query in queries :
        parents = []
        gen, order = query
        order -= 1
        if gen == 1 :
            answer.append('Rr')
            continue
        while gen != 1 :
            gen, order, rest = get_parents(gen, order)
            parents.append((gen, order, rest))
        parents = sorted(parents, key=lambda x : x[0])
        print(parents)
        for parent in parents :
            gen, order, rest = parent
            if gen == 1 and order == 0 :
                gene = 'Rr'
            gene = get_child_gene(gene, rest)
            print(gen + 1, gene)
        answer.append(gene)        
    return answer

if __name__=='__main__' :
    n = [[1, 1]]
    print(solution(n))