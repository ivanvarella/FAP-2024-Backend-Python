# def depositar(self, valor):
#         """Deposita um valor na conta, deve ser positivo."""
#         if valor > 0:
#             self.saldo += valor
#             self.operações.append(
#                 (datetime.now().strftime("%Y-%m-%d %H:%M"), "DEPÓSITO", valor)
#             )
#         else:
#             print("O valor do depósito deve ser positivo.")

#     def sacar(self, valor):
#         """Saca um valor da conta, utilizando o limite especial se necessário."""
#         if valor <= 0:
#             print("O valor do saque deve ser positivo.")
#             return

#         if self.saldo >= valor:
#             self.saldo -= valor
#             self.operações.append(
#                 (datetime.now().strftime("%Y-%m-%d %H:%M"), "SAQUE", -valor)
#             )
#         elif self.saldo + self.limite_especial >= valor:
#             self.saldo -= valor
#             self.operações.append(
#                 (datetime.now().strftime("%Y-%m-%d %H:%M"), "SAQUE LIMITE", -valor)
#             )
#             print(
#                 f"Saldo insuficiente. Usando limite especial. Novo saldo: R${self.saldo:.2f}"
#             )
#         else:
#             print(
#                 f"Saldo insuficiente. Seu saldo atual é de R${self.saldo:.2f} e seu limite especial é de R${self.limite_especial:.2f}."
#             )
