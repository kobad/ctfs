
write432:     file format elf32-i386


Disassembly of section .init:

080483c0 <_init>:
 80483c0:	53                   	push   %ebx
 80483c1:	83 ec 08             	sub    $0x8,%esp
 80483c4:	e8 e7 00 00 00       	call   80484b0 <__x86.get_pc_thunk.bx>
 80483c9:	81 c3 37 1c 00 00    	add    $0x1c37,%ebx
 80483cf:	8b 83 fc ff ff ff    	mov    -0x4(%ebx),%eax
 80483d5:	85 c0                	test   %eax,%eax
 80483d7:	74 05                	je     80483de <_init+0x1e>
 80483d9:	e8 92 00 00 00       	call   8048470 <memset@plt+0x10>
 80483de:	83 c4 08             	add    $0x8,%esp
 80483e1:	5b                   	pop    %ebx
 80483e2:	c3                   	ret    

Disassembly of section .plt:

080483f0 <printf@plt-0x10>:
 80483f0:	ff 35 04 a0 04 08    	pushl  0x804a004
 80483f6:	ff 25 08 a0 04 08    	jmp    *0x804a008
 80483fc:	00 00                	add    %al,(%eax)
	...

08048400 <printf@plt>:
 8048400:	ff 25 0c a0 04 08    	jmp    *0x804a00c
 8048406:	68 00 00 00 00       	push   $0x0
 804840b:	e9 e0 ff ff ff       	jmp    80483f0 <_init+0x30>

08048410 <fgets@plt>:
 8048410:	ff 25 10 a0 04 08    	jmp    *0x804a010
 8048416:	68 08 00 00 00       	push   $0x8
 804841b:	e9 d0 ff ff ff       	jmp    80483f0 <_init+0x30>

08048420 <puts@plt>:
 8048420:	ff 25 14 a0 04 08    	jmp    *0x804a014
 8048426:	68 10 00 00 00       	push   $0x10
 804842b:	e9 c0 ff ff ff       	jmp    80483f0 <_init+0x30>

08048430 <system@plt>:
 8048430:	ff 25 18 a0 04 08    	jmp    *0x804a018
 8048436:	68 18 00 00 00       	push   $0x18
 804843b:	e9 b0 ff ff ff       	jmp    80483f0 <_init+0x30>

08048440 <__libc_start_main@plt>:
 8048440:	ff 25 1c a0 04 08    	jmp    *0x804a01c
 8048446:	68 20 00 00 00       	push   $0x20
 804844b:	e9 a0 ff ff ff       	jmp    80483f0 <_init+0x30>

08048450 <setvbuf@plt>:
 8048450:	ff 25 20 a0 04 08    	jmp    *0x804a020
 8048456:	68 28 00 00 00       	push   $0x28
 804845b:	e9 90 ff ff ff       	jmp    80483f0 <_init+0x30>

08048460 <memset@plt>:
 8048460:	ff 25 24 a0 04 08    	jmp    *0x804a024
 8048466:	68 30 00 00 00       	push   $0x30
 804846b:	e9 80 ff ff ff       	jmp    80483f0 <_init+0x30>

Disassembly of section .plt.got:

08048470 <.plt.got>:
 8048470:	ff 25 fc 9f 04 08    	jmp    *0x8049ffc
 8048476:	66 90                	xchg   %ax,%ax

Disassembly of section .text:

08048480 <_start>:
 8048480:	31 ed                	xor    %ebp,%ebp
 8048482:	5e                   	pop    %esi
 8048483:	89 e1                	mov    %esp,%ecx
 8048485:	83 e4 f0             	and    $0xfffffff0,%esp
 8048488:	50                   	push   %eax
 8048489:	54                   	push   %esp
 804848a:	52                   	push   %edx
 804848b:	68 e0 86 04 08       	push   $0x80486e0
 8048490:	68 80 86 04 08       	push   $0x8048680
 8048495:	51                   	push   %ecx
 8048496:	56                   	push   %esi
 8048497:	68 7b 85 04 08       	push   $0x804857b
 804849c:	e8 9f ff ff ff       	call   8048440 <__libc_start_main@plt>
 80484a1:	f4                   	hlt    
 80484a2:	66 90                	xchg   %ax,%ax
 80484a4:	66 90                	xchg   %ax,%ax
 80484a6:	66 90                	xchg   %ax,%ax
 80484a8:	66 90                	xchg   %ax,%ax
 80484aa:	66 90                	xchg   %ax,%ax
 80484ac:	66 90                	xchg   %ax,%ax
 80484ae:	66 90                	xchg   %ax,%ax

080484b0 <__x86.get_pc_thunk.bx>:
 80484b0:	8b 1c 24             	mov    (%esp),%ebx
 80484b3:	c3                   	ret    
 80484b4:	66 90                	xchg   %ax,%ax
 80484b6:	66 90                	xchg   %ax,%ax
 80484b8:	66 90                	xchg   %ax,%ax
 80484ba:	66 90                	xchg   %ax,%ax
 80484bc:	66 90                	xchg   %ax,%ax
 80484be:	66 90                	xchg   %ax,%ax

080484c0 <deregister_tm_clones>:
 80484c0:	b8 33 a0 04 08       	mov    $0x804a033,%eax
 80484c5:	2d 30 a0 04 08       	sub    $0x804a030,%eax
 80484ca:	83 f8 06             	cmp    $0x6,%eax
 80484cd:	76 1a                	jbe    80484e9 <deregister_tm_clones+0x29>
 80484cf:	b8 00 00 00 00       	mov    $0x0,%eax
 80484d4:	85 c0                	test   %eax,%eax
 80484d6:	74 11                	je     80484e9 <deregister_tm_clones+0x29>
 80484d8:	55                   	push   %ebp
 80484d9:	89 e5                	mov    %esp,%ebp
 80484db:	83 ec 14             	sub    $0x14,%esp
 80484de:	68 30 a0 04 08       	push   $0x804a030
 80484e3:	ff d0                	call   *%eax
 80484e5:	83 c4 10             	add    $0x10,%esp
 80484e8:	c9                   	leave  
 80484e9:	f3 c3                	repz ret 
 80484eb:	90                   	nop
 80484ec:	8d 74 26 00          	lea    0x0(%esi,%eiz,1),%esi

080484f0 <register_tm_clones>:
 80484f0:	b8 30 a0 04 08       	mov    $0x804a030,%eax
 80484f5:	2d 30 a0 04 08       	sub    $0x804a030,%eax
 80484fa:	c1 f8 02             	sar    $0x2,%eax
 80484fd:	89 c2                	mov    %eax,%edx
 80484ff:	c1 ea 1f             	shr    $0x1f,%edx
 8048502:	01 d0                	add    %edx,%eax
 8048504:	d1 f8                	sar    %eax
 8048506:	74 1b                	je     8048523 <register_tm_clones+0x33>
 8048508:	ba 00 00 00 00       	mov    $0x0,%edx
 804850d:	85 d2                	test   %edx,%edx
 804850f:	74 12                	je     8048523 <register_tm_clones+0x33>
 8048511:	55                   	push   %ebp
 8048512:	89 e5                	mov    %esp,%ebp
 8048514:	83 ec 10             	sub    $0x10,%esp
 8048517:	50                   	push   %eax
 8048518:	68 30 a0 04 08       	push   $0x804a030
 804851d:	ff d2                	call   *%edx
 804851f:	83 c4 10             	add    $0x10,%esp
 8048522:	c9                   	leave  
 8048523:	f3 c3                	repz ret 
 8048525:	8d 74 26 00          	lea    0x0(%esi,%eiz,1),%esi
 8048529:	8d bc 27 00 00 00 00 	lea    0x0(%edi,%eiz,1),%edi

08048530 <__do_global_dtors_aux>:
 8048530:	80 3d 68 a0 04 08 00 	cmpb   $0x0,0x804a068
 8048537:	75 13                	jne    804854c <__do_global_dtors_aux+0x1c>
 8048539:	55                   	push   %ebp
 804853a:	89 e5                	mov    %esp,%ebp
 804853c:	83 ec 08             	sub    $0x8,%esp
 804853f:	e8 7c ff ff ff       	call   80484c0 <deregister_tm_clones>
 8048544:	c6 05 68 a0 04 08 01 	movb   $0x1,0x804a068
 804854b:	c9                   	leave  
 804854c:	f3 c3                	repz ret 
 804854e:	66 90                	xchg   %ax,%ax

08048550 <frame_dummy>:
 8048550:	b8 10 9f 04 08       	mov    $0x8049f10,%eax
 8048555:	8b 10                	mov    (%eax),%edx
 8048557:	85 d2                	test   %edx,%edx
 8048559:	75 05                	jne    8048560 <frame_dummy+0x10>
 804855b:	eb 93                	jmp    80484f0 <register_tm_clones>
 804855d:	8d 76 00             	lea    0x0(%esi),%esi
 8048560:	ba 00 00 00 00       	mov    $0x0,%edx
 8048565:	85 d2                	test   %edx,%edx
 8048567:	74 f2                	je     804855b <frame_dummy+0xb>
 8048569:	55                   	push   %ebp
 804856a:	89 e5                	mov    %esp,%ebp
 804856c:	83 ec 14             	sub    $0x14,%esp
 804856f:	50                   	push   %eax
 8048570:	ff d2                	call   *%edx
 8048572:	83 c4 10             	add    $0x10,%esp
 8048575:	c9                   	leave  
 8048576:	e9 75 ff ff ff       	jmp    80484f0 <register_tm_clones>

0804857b <main>:
 804857b:	8d 4c 24 04          	lea    0x4(%esp),%ecx
 804857f:	83 e4 f0             	and    $0xfffffff0,%esp
 8048582:	ff 71 fc             	pushl  -0x4(%ecx)
 8048585:	55                   	push   %ebp
 8048586:	89 e5                	mov    %esp,%ebp
 8048588:	51                   	push   %ecx
 8048589:	83 ec 04             	sub    $0x4,%esp
 804858c:	a1 64 a0 04 08       	mov    0x804a064,%eax
 8048591:	6a 00                	push   $0x0
 8048593:	6a 02                	push   $0x2
 8048595:	6a 00                	push   $0x0
 8048597:	50                   	push   %eax
 8048598:	e8 b3 fe ff ff       	call   8048450 <setvbuf@plt>
 804859d:	83 c4 10             	add    $0x10,%esp
 80485a0:	a1 40 a0 04 08       	mov    0x804a040,%eax
 80485a5:	6a 00                	push   $0x0
 80485a7:	6a 02                	push   $0x2
 80485a9:	6a 00                	push   $0x0
 80485ab:	50                   	push   %eax
 80485ac:	e8 9f fe ff ff       	call   8048450 <setvbuf@plt>
 80485b1:	83 c4 10             	add    $0x10,%esp
 80485b4:	83 ec 0c             	sub    $0xc,%esp
 80485b7:	68 00 87 04 08       	push   $0x8048700
 80485bc:	e8 5f fe ff ff       	call   8048420 <puts@plt>
 80485c1:	83 c4 10             	add    $0x10,%esp
 80485c4:	83 ec 0c             	sub    $0xc,%esp
 80485c7:	68 17 87 04 08       	push   $0x8048717
 80485cc:	e8 4f fe ff ff       	call   8048420 <puts@plt>
 80485d1:	83 c4 10             	add    $0x10,%esp
 80485d4:	e8 1d 00 00 00       	call   80485f6 <pwnme>
 80485d9:	83 ec 0c             	sub    $0xc,%esp
 80485dc:	68 1f 87 04 08       	push   $0x804871f
 80485e1:	e8 3a fe ff ff       	call   8048420 <puts@plt>
 80485e6:	83 c4 10             	add    $0x10,%esp
 80485e9:	b8 00 00 00 00       	mov    $0x0,%eax
 80485ee:	8b 4d fc             	mov    -0x4(%ebp),%ecx
 80485f1:	c9                   	leave  
 80485f2:	8d 61 fc             	lea    -0x4(%ecx),%esp
 80485f5:	c3                   	ret    

080485f6 <pwnme>:
 80485f6:	55                   	push   %ebp
 80485f7:	89 e5                	mov    %esp,%ebp
 80485f9:	83 ec 28             	sub    $0x28,%esp
 80485fc:	83 ec 04             	sub    $0x4,%esp
 80485ff:	6a 20                	push   $0x20
 8048601:	6a 00                	push   $0x0
 8048603:	8d 45 d8             	lea    -0x28(%ebp),%eax
 8048606:	50                   	push   %eax
 8048607:	e8 54 fe ff ff       	call   8048460 <memset@plt>
 804860c:	83 c4 10             	add    $0x10,%esp
 804860f:	83 ec 0c             	sub    $0xc,%esp
 8048612:	68 28 87 04 08       	push   $0x8048728
 8048617:	e8 04 fe ff ff       	call   8048420 <puts@plt>
 804861c:	83 c4 10             	add    $0x10,%esp
 804861f:	83 ec 0c             	sub    $0xc,%esp
 8048622:	68 51 87 04 08       	push   $0x8048751
 8048627:	e8 d4 fd ff ff       	call   8048400 <printf@plt>
 804862c:	83 c4 10             	add    $0x10,%esp
 804862f:	a1 60 a0 04 08       	mov    0x804a060,%eax
 8048634:	83 ec 04             	sub    $0x4,%esp
 8048637:	50                   	push   %eax
 8048638:	68 00 02 00 00       	push   $0x200
 804863d:	8d 45 d8             	lea    -0x28(%ebp),%eax
 8048640:	50                   	push   %eax
 8048641:	e8 ca fd ff ff       	call   8048410 <fgets@plt>
 8048646:	83 c4 10             	add    $0x10,%esp
 8048649:	90                   	nop
 804864a:	c9                   	leave  
 804864b:	c3                   	ret    

0804864c <usefulFunction>:
 804864c:	55                   	push   %ebp
 804864d:	89 e5                	mov    %esp,%ebp
 804864f:	83 ec 08             	sub    $0x8,%esp
 8048652:	83 ec 0c             	sub    $0xc,%esp
 8048655:	68 54 87 04 08       	push   $0x8048754
 804865a:	e8 d1 fd ff ff       	call   8048430 <system@plt>
 804865f:	83 c4 10             	add    $0x10,%esp
 8048662:	90                   	nop
 8048663:	c9                   	leave  
 8048664:	c3                   	ret    
 8048665:	66 90                	xchg   %ax,%ax
 8048667:	66 90                	xchg   %ax,%ax
 8048669:	66 90                	xchg   %ax,%ax
 804866b:	66 90                	xchg   %ax,%ax
 804866d:	66 90                	xchg   %ax,%ax
 804866f:	90                   	nop

08048670 <usefulGadgets>:
 8048670:	89 2f                	mov    %ebp,(%edi)
 8048672:	c3                   	ret    
 8048673:	66 90                	xchg   %ax,%ax
 8048675:	66 90                	xchg   %ax,%ax
 8048677:	66 90                	xchg   %ax,%ax
 8048679:	66 90                	xchg   %ax,%ax
 804867b:	66 90                	xchg   %ax,%ax
 804867d:	66 90                	xchg   %ax,%ax
 804867f:	90                   	nop

08048680 <__libc_csu_init>:
 8048680:	55                   	push   %ebp
 8048681:	57                   	push   %edi
 8048682:	56                   	push   %esi
 8048683:	53                   	push   %ebx
 8048684:	e8 27 fe ff ff       	call   80484b0 <__x86.get_pc_thunk.bx>
 8048689:	81 c3 77 19 00 00    	add    $0x1977,%ebx
 804868f:	83 ec 0c             	sub    $0xc,%esp
 8048692:	8b 6c 24 20          	mov    0x20(%esp),%ebp
 8048696:	8d b3 0c ff ff ff    	lea    -0xf4(%ebx),%esi
 804869c:	e8 1f fd ff ff       	call   80483c0 <_init>
 80486a1:	8d 83 08 ff ff ff    	lea    -0xf8(%ebx),%eax
 80486a7:	29 c6                	sub    %eax,%esi
 80486a9:	c1 fe 02             	sar    $0x2,%esi
 80486ac:	85 f6                	test   %esi,%esi
 80486ae:	74 25                	je     80486d5 <__libc_csu_init+0x55>
 80486b0:	31 ff                	xor    %edi,%edi
 80486b2:	8d b6 00 00 00 00    	lea    0x0(%esi),%esi
 80486b8:	83 ec 04             	sub    $0x4,%esp
 80486bb:	ff 74 24 2c          	pushl  0x2c(%esp)
 80486bf:	ff 74 24 2c          	pushl  0x2c(%esp)
 80486c3:	55                   	push   %ebp
 80486c4:	ff 94 bb 08 ff ff ff 	call   *-0xf8(%ebx,%edi,4)
 80486cb:	83 c7 01             	add    $0x1,%edi
 80486ce:	83 c4 10             	add    $0x10,%esp
 80486d1:	39 f7                	cmp    %esi,%edi
 80486d3:	75 e3                	jne    80486b8 <__libc_csu_init+0x38>
 80486d5:	83 c4 0c             	add    $0xc,%esp
 80486d8:	5b                   	pop    %ebx
 80486d9:	5e                   	pop    %esi
 80486da:	5f                   	pop    %edi
 80486db:	5d                   	pop    %ebp
 80486dc:	c3                   	ret    
 80486dd:	8d 76 00             	lea    0x0(%esi),%esi

080486e0 <__libc_csu_fini>:
 80486e0:	f3 c3                	repz ret 

Disassembly of section .fini:

080486e4 <_fini>:
 80486e4:	53                   	push   %ebx
 80486e5:	83 ec 08             	sub    $0x8,%esp
 80486e8:	e8 c3 fd ff ff       	call   80484b0 <__x86.get_pc_thunk.bx>
 80486ed:	81 c3 13 19 00 00    	add    $0x1913,%ebx
 80486f3:	83 c4 08             	add    $0x8,%esp
 80486f6:	5b                   	pop    %ebx
 80486f7:	c3                   	ret    
