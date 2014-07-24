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

relogio = [[0] for i in range(processos)]
log = []
count = 0

while(count < eventos):
    print "Qual processo envia a mensagem?"
    p_envia = int(raw_input("=> "))

    print "Qual processo recebe a mensagem?"
    p_recebe = int(raw_input("=> "))

    if p_envia == p_recebe:
        relogio[p_envia].append(relogio[p_envia][-1] + 1)
        relogio[p_recebe].append(relogio[p_recebe][-1] + 1)
        print "\n# TIPO: Evento Interno"
        print "# M = %s" % relogio[p_envia][-2]
        print "# R de P%s = %s\n" % (p_envia, relogio[p_envia][-1])
    else:
        relogio[p_envia].append(relogio[p_envia][-1] + 1)
        print "\n# TIPO: Evento Entre Processos"
        print "# M = %s" % relogio[p_envia][-1]
        print "# R de P%s = %s" % (p_envia, relogio[p_envia][-1])

        if relogio[p_envia][-1] > relogio[p_recebe][-1]:
            relogio[p_recebe].append(relogio[p_envia][-1] + 1)
            print "# R de P%s = %s" % (p_recebe, relogio[p_recebe][-1])
        else:
            relogio[p_recebe].append(relogio[p_recebe][-1] + 1)
            print "# R de P%s = %s" % (p_recebe, relogio[p_recebe][-1])

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
