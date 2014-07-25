#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Digite o número de processos:"
processos = int(raw_input("=> "))

print "Digite o número de eventos:"
eventos = int(raw_input("=> "))

print "\n=========================="
print "Lista de processos: "

for i in range(processos):
    print i,

print "\n"

relogio = [[0 for i in range(processos)] for i in range(processos)]
log = []
count = 0

while count < eventos:
    print "Qual processo envia a mensagem?"
    p_envia = int(raw_input("=> "))

    print "Qual processo recebe a mensagem?"
    p_recebe = int(raw_input("=> "))

    relogio[p_envia][p_envia] = relogio[p_envia][p_envia] + 1

    if p_envia == p_recebe:
        print "\n# TIPO: Evento Interno"
        print "# M = %s" % relogio[p_envia]
        print "# R de P%s = %s\n" % (p_envia, relogio[p_envia])
    else:
        count2 = 0
        print "\n# TIPO: Evento Entre Processos"
        print "# M = %s" % relogio[p_envia]
        print "# R de P%s = %s" % (p_envia, relogio[p_envia])

        while count2 < processos:
            if relogio[p_envia][count2] > relogio[p_recebe][count2]:
                relogio[p_recebe][count2] = relogio[p_envia][count2]

            count2 = count2 + 1

        relogio[p_recebe][p_recebe] = relogio[p_recebe][p_recebe] + 1
        print "# R de P%s = %s\n" % (p_recebe, relogio[p_recebe])

    log.append("[%s]---->" % p_envia)
    log.append("[%s]" % p_recebe)
    count = count + 1

print "\n"
print "Histórico: ",
for l in log:
    print l,
print "\n"

i=0

for r in relogio:
    print "Relógio de P%s:" % i,
    print r
    i = i + 1
print "\n"