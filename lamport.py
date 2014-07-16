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
        print "m = %s" % relogio[p_envia][-1]
        relogio[p_envia].append(relogio[p_envia][-1] + 1)
    else:
        if relogio[p_envia][-1] > relogio[p_recebe][-1]:
            print "m = %s" % relogio[p_envia][-1]
            relogio[p_recebe].append(relogio[p_envia][-1] + 1)
        else:
            print "m = %s" % relogio[p_envia][-1]
            relogio[p_recebe].append(relogio[p_recebe][-1] + 1)

    log.append("[%s]---->" % p_envia)
    log.append("[%s]" % p_recebe)
    count = count + 1

print "\n"

for l in log:
    print l,
print "\n"

i=0

for r in relogio:
    print "Clock %s:" % i,
    print r
    i = i + 1
print "\n"
