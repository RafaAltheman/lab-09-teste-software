
## Ex1

### a) Cobertura inicial e mutantes

A suíte inicial contém dois testes: um aluno aprovado, com média 8,0 e presença de 80%, e um aluno reprovado por nota, com média 3,0 e presença de 90%.

Os dois testes foram executados com sucesso.

A cobertura inicial de ramos foi de **60% (6 de 10 ramos)**, enquanto a cobertura combinada apresentada pelo pytest-cov foi de 64%.

Isso ocorre porque a suíte inicial não testa todas as possibilidades de classificação nem as validações de entradas inválidas.

Resultados dos mutantes:

- Mutantes gerados: [preencher após executar mutmut]
- Mutantes mortos: [preencher]
- Mutantes vivos: [preencher]

### b) Causas dos mutantes vivos

Os mutantes sobreviventes podem ser agrupados de acordo com os comportamentos que não são verificados pelos testes iniciais.

**Validação de dados:** os testes iniciais não fornecem médias negativas, maiores que 10, presenças negativas ou superiores a 100. Dessa forma, mutações nas verificações desses limites podem sobreviver.

**Classificações não exercitadas:** os testes não verificam a recuperação nem a reprovação por falta. Mutações nas instruções responsáveis por esses resultados não são detectadas.

**Condições de fronteira:** não existem testes próximos às médias 5,0 e 7,0 nem ao limite de presença de 75%. Por isso, alterações nos operadores de comparação podem passar despercebidas.

As linhas do código original não executadas incluem as linhas 3, 5, 7 e 11, correspondentes às exceções, à reprovação por falta e à recuperação.

A identificação específica de cada mutante deve ser realizada utilizando os comandos `mutmut results` e `mutmut show`.

### c) Melhoria da suíte e escore final

A suíte foi ampliada para incluir testes dos valores-limite, situações de recuperação, reprovação por falta, presença mínima exigida e entradas inválidas.

Foram adicionados testes para médias iguais a 5,0 e 7,0, valores próximos desses limites, presença de 75%, frequência abaixo do mínimo e valores fora das faixas permitidas.

Após as melhorias, os 20 casos de teste passaram e a cobertura de ramos chegou a **100%**.

As mutações nas condições de classificação e nas validações de entrada podem ser diferenciadas do programa original por entradas apropriadas.

Entretanto, a existência de mutantes equivalentes deve ser confirmada individualmente, pois nem toda alteração produz um comportamento observavelmente diferente.

O escore é calculado por:

MS = mortos / (gerados - equivalentes) × 100%

- Mutantes equivalentes: [preencher]
- MS inicial: [preencher]
- MS final: [preencher]

### d) Verificação de exceções com pytest.raises

Ao utilizar `pytest.raises(ValueError, match=msg)`, o teste passa a verificar tanto o tipo da exceção quanto a mensagem apresentada.

Anteriormente, verificar apenas a ocorrência de `ValueError` permitiria que modificações no texto da mensagem não fossem detectadas.

A utilização de `match` permite identificar essas alterações e aumentar a capacidade da suíte de detectar erros.

Como `match` interpreta uma expressão regular, foram usados os delimitadores `^` e `$` para conferir as mensagens completas.

---

## Exercício 2 — Desconto Progressivo

### a) Cobertura de ramos e escore inicial

A suíte inicial realiza uma única verificação, confirmando que o resultado do carrinho é maior que zero.

Apesar de simples, esse teste percorre os dois caminhos da condição que determina a aplicação do desconto.

Por isso, a cobertura de ramos obtida foi de **100% (4 de 4 ramos)**.

Entretanto, a cobertura elevada não significa que a suíte seja eficaz.

Um resultado incorreto continuaria passando no teste desde que fosse positivo.

Portanto, a cobertura mede os caminhos executados, enquanto o escore de mutação mede a capacidade dos testes de perceber mudanças no comportamento do programa.

- Mutantes gerados: [preencher]
- Mutantes mortos: [preencher]
- Mutantes vivos: [preencher]
- MS inicial: [preencher]

### b) Alteração do assert para o valor exato

Foi mantida a lista de preços original:

[10, 20, 30, 40, 50]

Os três primeiros itens não recebem desconto, enquanto o quarto e o quinto recebem 10%.

O cálculo correto é:

10 + 20 + 30 + 36 + 45 = 141,00

O teste foi alterado para verificar exatamente esse valor:

`assert total_com_desconto([10, 20, 30, 40, 50]) == 141.00`

A cobertura de ramos permanece em 100%, porque o caminho executado não mudou.

Porém, a verificação se tornou mais rigorosa e passou a detectar alterações que modificam o resultado esperado.

- Mutantes vivos após a alteração: [preencher]

### c) Classificação dos mutantes sobreviventes

A análise dos sobreviventes considera quatro condições fundamentais.

**Alcançar:** o teste deve executar o trecho do programa que sofreu a mutação.

**Infectar:** a mutação deve causar uma diferença no estado interno ou em algum resultado intermediário.

**Propagar:** essa diferença precisa alcançar uma saída observável do programa.

**Revelar:** a verificação do teste deve identificar a diferença e provocar uma falha.

Na suíte inicial, diversos mutantes podem ser alcançados, provocar alterações e propagar um resultado diferente, mas permanecer vivos porque o teste verifica apenas se o total é positivo.

Após substituir o assert pelo valor exato, mutantes que alteram o resultado numérico podem ser detectados.

Outras mutações podem continuar sobrevivendo quando a entrada utilizada não produz diferenças observáveis, como mudanças na precisão do arredondamento que não afetam um total inteiro.

A classificação definitiva de cada sobrevivente deve ser feita com `mutmut show`.

### d) Novas entradas e escore final

Foram acrescentados testes com listas vazias, listas contendo menos de quatro itens, listas com exatamente quatro itens e diferentes combinações de preços.

Também foram utilizados preços iguais a zero e preços fracionários.

Essas entradas permitem verificar o início da aplicação do desconto e o arredondamento do resultado.

O caso `[0, 0, 0, 0.03]` é especialmente importante.

O desconto produz o valor intermediário de 0,027, que deve ser arredondado para 0,03.

Portanto, os preços fracionários são fundamentais para revelar mutações que alteram a precisão do arredondamento.

A suíte final contém 10 casos de teste, todos aprovados, com cobertura de ramos de 100%.

- MS final: [preencher após executar mutmut]

---

## Exercício 3 — Temperaturas da Semana

### a) Implementação inicial e mutantes vivos

A suíte inicial utiliza as listas:

- [21, 25, 19, 30, 22]
- [18]
- [30, 21]

Também são realizadas verificações com listas vazias, esperando a ocorrência de `ValueError`.

As duas funções são testadas com os valores exatos esperados.

A cobertura inicial de ramos foi de **100% (12 de 12 ramos)**.

Entretanto, a suíte não verifica situações em que a maior temperatura aparece repetidamente.

Assim, alguns mutantes podem sobreviver mesmo com todos os ramos executados.

- Mutantes vivos: [preencher]
- Identificadores e alterações: [preencher com mutmut show]

### b) Mutantes equivalentes e não equivalentes

Na função `maior`, uma mutação que substitui `>` por `>=` é equivalente ao programa original.

Isso acontece porque, quando duas temperaturas são iguais, a atribuição realizada pelo mutante não modifica o valor máximo armazenado.

Consequentemente, o valor retornado permanece o mesmo.

Na função `dia_do_maior`, a mesma alteração não é equivalente.

A especificação determina que a função deve devolver a posição do primeiro dia em que ocorreu a maior temperatura.

Com o operador `>=`, a posição seria atualizada em caso de empate, fazendo a função devolver o último dia que apresentou o valor máximo.

Portanto, a alteração modifica o comportamento exigido pela especificação.

Mutações apenas nas mensagens das exceções devem ser avaliadas conforme a exigência de validar somente o tipo do erro ou também seu texto.

### c) Melhoria da suíte e comparação dos escores

Foram acrescentadas listas com temperaturas máximas repetidas e diferentes posições para o maior valor.

Entre os novos casos estão:

- [30, 21, 30]
- [20, 25, 25, 10]
- [7, 7, 7]
- [1, 9, 2]

Esses testes permitem verificar se a função `dia_do_maior` realmente devolve a primeira posição da temperatura máxima.

Também foram incluídos casos com temperaturas negativas, listas crescentes e verificação da mensagem de erro para listas vazias.

Após as alterações, os 12 casos de teste passaram e a cobertura de ramos continuou em 100%.

- MS inicial: [preencher]
- Mutantes não equivalentes mortos: [preencher]
- Mutantes equivalentes: [preencher]
- MS final ajustado: [preencher]

### d) Diferença entre as duas funções

A equivalência depende do comportamento observável exigido pela especificação.

Na função `maior`, o resultado é o próprio valor da maior temperatura. Atualizar o valor armazenado quando ocorre um empate não modifica a resposta.

Já na função `dia_do_maior`, o resultado é uma posição da lista.

Quando a condição passa de `>` para `>=`, empates provocam atualizações indevidas da posição, contrariando o requisito de retornar a primeira ocorrência.

Assim, a mesma mutação pode ser equivalente em uma função e não equivalente em outra.

---

## Exercício 4 — Parcelamento

### a) Suíte construída por análise de valor-limite

A função permite parcelamentos entre 1 e 12 parcelas.

Valores fora desse intervalo devem produzir uma exceção `ValueError`.

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

### b) Cobertura e escore de mutação

A suíte inicial de valor-limite contém 10 casos de teste.

Todos foram executados com sucesso, e a cobertura de ramos obtida foi de **100% (4 de 4 ramos)**.

Os testes percorrem os caminhos de validação de parcelas, o cálculo sem juros e o cálculo com juros.

A cobertura elevada demonstra que as principais decisões do programa foram exercitadas.

Entretanto, isso não garante que todas as mutações sejam detectadas, pois certas alterações podem produzir resultados iguais para os valores utilizados.

- Mutantes gerados: [preencher]
- Mutantes mortos: [preencher]
- Mutantes vivos: [preencher]
- MS inicial: [preencher]

### c) Análise dos sobreviventes e escore final

Para melhorar a suíte, foram incluídos testes com valores intermediários de parcelas, valores monetários fracionários e situações que exigem arredondamento.

A suíte final contém 18 casos de teste, todos aprovados, mantendo 100% de cobertura de ramos.

Um exemplo importante de mutante equivalente é a alteração da condição `n <= 3` para `n < 3`.

Na versão original, três parcelas entram no ramo sem juros.

Na versão mutante, três parcelas entram no ramo que calcula juros.

Entretanto, o cálculo realizado nesse caso é:

`0.02 * (3 - 3) = 0`

Assim, as duas versões produzem exatamente o mesmo resultado para três parcelas, e os demais valores continuam seguindo fórmulas equivalentes.

Essa mutação não pode ser eliminada por testes, pois não modifica o comportamento observável da função.

Os demais sobreviventes devem ser analisados individualmente, verificando alterações nos limites de parcelas, na fórmula de juros, nas operações aritméticas e no arredondamento.

Quando uma mutação modifica o resultado para alguma entrada válida, novos testes podem ser adicionados para eliminá-la.

Quando a mutação não altera nenhum resultado observável, deve ser classificada como equivalente.

O escore final deve excluir os mutantes equivalentes do denominador.

- Mutantes mortos após as melhorias: [preencher]
- Mutantes equivalentes identificados: [preencher]
- MS final: [preencher]

