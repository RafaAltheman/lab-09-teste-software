

## Resumo dos resultados

Os testes foram executados em ambiente Linux, utilizando pytest 9.1.1, pytest-cov 7.1.0 e mutmut 3.8.0.

| Exercício | Gerados | Mortos iniciais | Vivos iniciais | Mortos finais | Equivalentes | MS final |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 36 | 6 | 30 | 36 | 0 | 100% |
| 2 | 16 | 4 | 12 | 16 | 0 | 100% |
| 3 | 22 | 11 | 11 | 20 | 2 | 100% |
| 4 | 27 | 26 | 1 | 26 | 1 | 100% |


## Ex1

### a) 

A suíte inicial contém dois testes: um aluno aprovado, com média 8,0 e presença de 80%, e um aluno reprovado por nota, com média 3,0 e presença de 90%.

Os dois testes foram executados com sucesso.

A cobertura inicial combinada foi de **64%**, enquanto a cobertura específica de ramos foi de **60% (6 de 10 ramos)**.

As linhas 3, 5, 7 e 11 não foram executadas, pois a suíte não testa entradas inválidas, reprovação por falta nem recuperação.

Resultados obtidos com o mutmut:

- Mutantes gerados: 36
- Mutantes mortos: 6
- Mutantes vivos: 30
- Mutantes equivalentes: 0
- MS inicial: 6/36 × 100% = **16,7%**

O resultado mostra que a suíte inicial possui baixa capacidade de identificar alterações no código, pois verifica apenas dois comportamentos específicos.

### b) 

Os 30 mutantes sobreviventes foram agrupados de acordo com a causa de sua sobrevivência.

| Grupo | Mutantes | Quantidade | Condição que falhou |
|---|---|---:|---|
| Alterações em linhas não executadas | 6–9, 15–18, 21–23, 31–33 | 14 | Alcançar |
| Alterações em condições executadas, mas sem entradas capazes de mudar as decisões | 1–5, 10–14, 19–20, 24–25, 29–30 | 16 | Infectar |

Os 14 mutantes do primeiro grupo estão associados às linhas 3, 5, 7 e 11, que não são executadas pela suíte inicial. Essas linhas contêm as mensagens das exceções e os retornos referentes à reprovação por falta e à recuperação.

Os outros 16 mutantes estão relacionados às validações de média e presença e às condições que determinam a classificação do aluno.

Apesar de algumas dessas condições serem executadas, os valores utilizados nos testes não conseguem diferenciar o comportamento original do comportamento mutante.

Isso ocorre porque os testes utilizam valores distantes das fronteiras, sem explorar os limites das comparações.

### c) 

A suíte foi ampliada para incluir testes dos valores-limite, situações de recuperação, reprovação por falta, presença mínima exigida e entradas inválidas.

Foram adicionados casos com médias iguais a 5,0 e 7,0 e valores próximos desses limites, além de presenças iguais a 75%, inferiores ao mínimo e próximas dos extremos permitidos.

Também foram incluídas entradas inválidas, com médias negativas ou superiores a 10 e presenças negativas ou superiores a 100.

As mensagens de erro passaram a ser verificadas com expressões regulares ancoradas, garantindo a correspondência com o texto completo.

Após as melhorias, os 20 casos de teste passaram e a cobertura chegou a **100% dos ramos**.

Resultados finais:

- Mutantes gerados: 36
- Mutantes mortos: 36
- Mutantes vivos: 0
- Mutantes equivalentes: 0
- MS final: 36/(36 - 0) × 100% = **100%**

A suíte melhorada conseguiu eliminar todos os mutantes gerados, demonstrando maior capacidade de detectar alterações nas condições, nos retornos e nas validações.

### d) 

Ao utilizar `pytest.raises(ValueError, match=msg)`, o teste passa a verificar tanto o tipo da exceção quanto a correspondência da mensagem com uma expressão regular.

Entretanto, existe uma diferença importante entre essa abordagem e a comparação por igualdade exata.

O parâmetro `match` utiliza uma busca por expressão regular. Assim, uma mensagem como `"XXMedia invalidaXX"` ainda corresponde ao padrão `"Media invalida"`, mesmo contendo caracteres adicionais.

Isso pode permitir a sobrevivência de mutantes que modificam a mensagem acrescentando caracteres antes ou depois do texto esperado.

Na suíte final utilizada neste laboratório, foram empregados os delimitadores `^` e `$`, como em:

`pytest.raises(ValueError, match=r"^Media invalida$")`

Dessa forma, a expressão verifica a mensagem inteira, evitando que textos adicionais sejam aceitos.

Com essa verificação, os 36 mutantes foram mortos e o MS permaneceu em 100%.

Conclui-se que `match` sem delimitadores pode ser menos rigoroso do que uma comparação exata, mas é possível fortalecer essa verificação utilizando expressões regulares ancoradas.

---

## Ex2

### a) 

A suíte inicial realiza uma única verificação, confirmando que o resultado do carrinho é maior que zero:

`assert total_com_desconto([10, 20, 30, 40, 50]) > 0`

Apesar de simples, esse teste percorre os dois caminhos da condição que determina a aplicação do desconto.

Por isso, a cobertura de ramos obtida foi de **100% (4 de 4 ramos)**.

Entretanto, a cobertura elevada não significa que a suíte seja eficaz.

Um resultado incorreto continuaria passando no teste desde que fosse positivo.

Resultados do mutmut:

- Mutantes gerados: 16
- Mutantes mortos: 4
- Mutantes vivos: 12
- MS inicial: 4/16 × 100% = **25%**

Os resultados demonstram que cobertura e escore de mutação medem características diferentes.

A cobertura indica quais partes do código foram executadas, enquanto o escore de mutação avalia a capacidade dos testes de identificar alterações no comportamento do programa.

### b) 

Foi mantida a lista de preços original:

`[10, 20, 30, 40, 50]`

Os três primeiros itens não recebem desconto, enquanto o quarto e o quinto recebem 10%.

O cálculo correto é:

10 + 20 + 30 + 36 + 45 = 141,00

O teste foi alterado para verificar exatamente esse valor:

`assert total_com_desconto([10, 20, 30, 40, 50]) == 141.00`

A cobertura de ramos permaneceu em 100%, porque os caminhos executados não mudaram.

Porém, a verificação se tornou mais rigorosa e passou a detectar alterações que modificam o resultado numérico.

Após essa alteração, os resultados foram:

- Mutantes gerados: 16
- Mutantes mortos: 13
- Mutantes vivos: 3
- MS intermediário: 13/16 × 100% = **81,25%**

Os três sobreviventes estavam relacionados ao arredondamento:

- Mutante 13: alteração para `round(total, None)`
- Mutante 15: remoção da precisão, equivalente a `round(total)`
- Mutante 16: alteração para `round(total, 3)`

Como o resultado do teste utilizado era 141,00, essas mudanças não provocaram uma diferença numérica detectável pela comparação.

### c) 
A análise considera quatro condições fundamentais:

**Alcançar:** o teste precisa executar a instrução modificada.

**Infectar:** a mutação precisa provocar uma diferença no estado interno ou no resultado intermediário.

**Propagar:** essa diferença deve chegar a uma saída observável.

**Revelar:** o teste precisa detectar essa diferença por meio de sua verificação.

Os três mutantes sobreviventes estão relacionados à operação de arredondamento.

| Mutante | Condição que falhou | Justificativa |
|---|---|---|
| `round(total, None)` | Revelar | Retorna o inteiro 141 em vez do float 141.0, mas a igualdade numérica considera os valores iguais. |
| `round(total)` | Revelar | O arredondamento sem precisão explícita também retorna 141, que passa na comparação com 141.0. |
| `round(total, 3)` | Infectar | Como o total é 141.0, arredondar para duas ou três casas não modifica o valor. |

Nos dois primeiros casos, existe uma diferença no tipo do resultado, mas o `assert` utiliza igualdade numérica, que não distingue `141` de `141.0`.

No terceiro caso, a própria entrada escolhida não produz diferença no valor retornado.

### d) 

Foram acrescentados testes com listas vazias, listas contendo menos de quatro itens, listas com exatamente quatro itens e diferentes combinações de preços.

Também foram utilizados preços iguais a zero e preços fracionários.

Essas entradas permitem verificar o início da aplicação do desconto e o arredondamento do resultado.

Um caso importante é:

`[0, 0, 0, 0.03]`

O desconto produz o valor intermediário de 0,027, que deve ser arredondado para 0,03.

Caso a precisão seja alterada para três casas decimais, o resultado será 0,027, permitindo detectar a mutação.

Outro caso relevante é:

`[0, 0, 0, 1.11]`

O resultado intermediário é 0,999, que deve ser arredondado para 1,00.

Portanto, os preços fracionários foram fundamentais para revelar mutações que alteravam a precisão do arredondamento.

A suíte final contém 10 casos de teste, todos aprovados, com cobertura de ramos de 100%.

Resultados finais:

- Mutantes gerados: 16
- Mutantes mortos: 16
- Mutantes vivos: 0
- Mutantes equivalentes: 0
- MS final: 16/16 × 100% = **100%**

A alteração do assert aumentou significativamente o escore, enquanto os testes com preços fracionários eliminaram os mutantes restantes.

---

## Ex3

### a) 

A suíte inicial utiliza as listas:

- `[21, 25, 19, 30, 22]`
- `[18]`
- `[30, 21]`

Também são realizadas verificações com listas vazias, esperando a ocorrência de `ValueError`.

As duas funções são testadas com os valores exatos esperados.

A cobertura inicial de ramos foi de **100% (12 de 12 ramos)**.

Entretanto, a suíte não verifica situações em que a maior temperatura aparece repetidamente nem confere a mensagem das exceções.

Resultados do mutmut:

- Mutantes gerados: 22
- Mutantes mortos: 11
- Mutantes vivos: 11
- MS inicial bruto: 11/22 × 100% = **50%**

Os mutantes sobreviventes identificados foram:

| Função | Mutantes vivos | Alteração |
|---|---|---|
| `maior` | 2, 3 e 4 | Modificações na mensagem da exceção |
| `maior` | 7 | `temps[1:]` alterado para `temps[2:]` |
| `maior` | 8 | Comparação `>` alterada para `>=` |
| `dia_do_maior` | 2, 3 e 4 | Modificações na mensagem da exceção |
| `dia_do_maior` | 9 | `range(1, len(temps))` alterado para `range(len(temps))` |
| `dia_do_maior` | 11 | `range(1, len(temps))` alterado para `range(2, len(temps))` |
| `dia_do_maior` | 12 | Comparação `>` alterada para `>=` |

### b)

Os mutantes foram classificados considerando o comportamento observável exigido pela especificação.

| Mutante | Equivalente? | Justificativa |
|---|---|---|
| `maior` 2, 3 e 4 | Não | Modificam a mensagem do erro, que pode ser verificada por um teste. |
| `maior` 7 | Não | Ignora o elemento do índice 1, podendo deixar de encontrar a maior temperatura. |
| `maior` 8 | Sim | Substituir `>` por `>=` não modifica o valor máximo retornado. |
| `dia_do_maior` 2, 3 e 4 | Não | Modificam a mensagem da exceção. |
| `dia_do_maior` 9 | Sim | Apenas acrescenta a comparação do primeiro elemento com ele mesmo. |
| `dia_do_maior` 11 | Não | Ignora o elemento do índice 1, podendo retornar uma posição incorreta. |
| `dia_do_maior` 12 | Não | Em caso de empate, retorna a última ocorrência em vez da primeira. |

Na função `maior`, uma mutação que substitui `>` por `>=` é equivalente ao programa original.

Isso acontece porque, quando duas temperaturas são iguais, a atribuição realizada pelo mutante não modifica o valor máximo armazenado.

Na função `dia_do_maior`, o mutante que altera o início do intervalo de `range(1, len(temps))` para `range(len(temps))` também é equivalente.

A única iteração adicional é a de índice zero, em que a comparação `temps[0] > temps[0]` é falsa. Portanto, a posição armazenada não muda.

Já a substituição de `>` por `>=` na função `dia_do_maior` não é equivalente, pois altera a posição retornada quando existem temperaturas máximas repetidas.

Assim, foram identificados **2 mutantes equivalentes** entre os 22 gerados.

### c) 
Foram acrescentadas listas com temperaturas máximas repetidas e diferentes posições para o maior valor.

Entre os novos casos estão:

- `[30, 21, 30]`
- `[20, 25, 25, 10]`
- `[7, 7, 7]`
- `[1, 9, 2]`

Esses testes permitem verificar se a função `dia_do_maior` realmente devolve a primeira posição da temperatura máxima.

Também foram incluídos casos com temperaturas negativas, listas crescentes e verificação da mensagem completa de erro para listas vazias.

Após as alterações, os 12 casos de teste passaram e a cobertura de ramos continuou em 100%.

Resultados iniciais:

- Mutantes gerados: 22
- Mutantes mortos: 11
- Mutantes vivos: 11
- Mutantes equivalentes: 2
- MS inicial bruto: 11/22 × 100% = **50%**
- MS inicial ajustado: 11/(22 - 2) × 100% = **55%**

Resultados finais:

- Mutantes mortos: 20
- Mutantes vivos: 2
- Mutantes equivalentes: 2
- MS final bruto: 20/22 × 100% = **90,9%**
- MS final ajustado: 20/(22 - 2) × 100% = **100%**

Os dois mutantes sobreviventes são justamente os equivalentes identificados anteriormente.

Dessa forma, todos os mutantes não equivalentes foram eliminados pela suíte.

### d)

A equivalência depende do comportamento observável exigido pela especificação.

Na função `maior`, o resultado é o próprio valor da maior temperatura.

Atualizar o valor armazenado quando ocorre um empate não modifica a resposta, pois os valores são iguais.

Já na função `dia_do_maior`, o resultado é uma posição da lista.

Quando a condição passa de `>` para `>=`, empates provocam atualizações indevidas da posição, contrariando o requisito de retornar a primeira ocorrência.

Por exemplo:

`dia_do_maior([30, 21, 30])`

O programa original retorna 0, enquanto o mutante com `>=` retorna 2.

Assim, a mesma mutação pode ser equivalente em uma função e não equivalente em outra.

---

## Ex4

### a) 

A função permite parcelamentos entre 1 e 12 parcelas.

Valores fora desse intervalo devem produzir uma exceção `ValueError("parcelas invalidas")`.

Além disso, até três parcelas não são cobrados juros. A partir da quarta parcela, aplica-se um acréscimo de 2% por parcela adicional à terceira.

Com base nessa especificação, foram definidos testes próximos aos limites do intervalo permitido e da mudança na regra de juros.

Para uma compra de R$ 100,00:

| Parcelas | Resultado esperado |
|---|---|
| 1 | R$ 100,00 |
| 2 | R$ 50,00 |
| 3 | R$ 33,33 |
| 4 | R$ 25,50 |
| 11 | R$ 10,55 |
| 12 | R$ 9,83 |

Os valores -1, 0, 13 e 14 foram utilizados para verificar entradas inválidas.

Essa suíte permite avaliar os limites inferior e superior e a transição entre parcelamentos com e sem juros.

A análise foi realizada antes da execução das ferramentas, conforme solicitado no enunciado.

### b) 

A suíte inicial de valor-limite contém 10 casos de teste.

Todos foram executados com sucesso, e a cobertura de ramos obtida foi de **100% (4 de 4 ramos)**.

Os testes percorrem os caminhos de validação de parcelas, o cálculo sem juros e o cálculo com juros.

Resultados do mutmut:

- Mutantes gerados: 27
- Mutantes mortos: 26
- Mutantes vivos: 1
- MS inicial bruto: 26/27 × 100% = **96,3%**

O resultado demonstra que a análise de valor-limite conseguiu detectar praticamente todas as alterações geradas pelo mutmut.

O único mutante sobrevivente está relacionado a uma condição de comparação que, apesar de modificada, não altera o resultado calculado.

### c) 

O único mutante sobrevivente foi a alteração da condição:

`if n <= 3`

para:

`if n < 3`

Essa mutação é equivalente ao programa original.

Na versão original, três parcelas entram no ramo sem juros, atribuindo zero à variável `juros`.

Na versão mutante, três parcelas entram no ramo que calcula os juros pela fórmula:

`juros = 0.02 * (n - 3)`

Entretanto, quando `n = 3`, o cálculo realizado é:

`0.02 * (3 - 3) = 0`

Assim, as duas versões produzem exatamente o mesmo resultado para três parcelas.

Nos demais valores, o comportamento também permanece igual.

Dessa forma, a mutação não pode ser eliminada por testes, pois não modifica o resultado observável da função.

A suíte foi ampliada para incluir valores intermediários de parcelas, valores monetários fracionários e situações que exigem arredondamento.

A suíte final contém 18 casos de teste, todos aprovados, mantendo 100% de cobertura de ramos.

Resultados finais:

- Mutantes gerados: 27
- Mutantes mortos: 26
- Mutantes vivos: 1
- Mutantes equivalentes: 1
- MS final bruto: 26/27 × 100% = **96,3%**
- MS final ajustado: 26/(27 - 1) × 100% = **100%**

Os testes adicionais reforçaram a verificação do comportamento, mas não aumentaram a quantidade de mutantes mortos, pois a suíte inicial já eliminava todos os mutantes não equivalentes.

Conclui-se que a análise de valor-limite foi bastante eficaz nesse exercício, permitindo atingir o escore máximo ajustado sem necessidade de eliminar o mutante equivalente.

