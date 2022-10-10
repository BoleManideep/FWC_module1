.include "/home/manideep/FWC/Assignements/assembly/codes/m328Pdef.inc"

	ldi r17, 0b11000011 ; identifying input pins 2(U),3(V),4(W),5(Z)
	out DDRD,r17		; declaring pins as input
	
	ldi r17, 0b11111111 ;
	out PORTD,r17		; activating internal pullup for pins
	
	loop:
	in r17,PIND
	
	ldi r16, 0b00000010 ;  declaring 9th pin as output
	out DDRB,r16		
	
	MOV r18,r17  ;U
	MOV r19,r17  ;V
	MOV r20,r17  ;W
	MOV r21,r17  ;Z
	
	ldi r22,0b00000100
	AND r18,r22
	ldi r30,0b00000010 ; counter=2
	rcall loopu	
	
	ldi r23,0b00001000
	AND r19,r23
	ldi r31,0b00000011 ; counter=3
	rcall loopv
	
	ldi r24,0b00010000
	AND r20,r24
	ldi r29,0b00000100 ; counter=4
	rcall loopw
	
	ldi r25,0b00100000
	AND r21,r25
	ldi r28,0b00000101 ; counter=5
	rcall loopz
	
	ldi r26,0b00000001
	EOR r19,r26 		; !V
	
	ldi r27,0b00000001
	EOR r20,r27 		; !W
	
	OR r18,r19
	AND r20,r18
	OR r21,r20
	
	ldi r28,0b00000001
	rcall loopf
	OUT PORTB,r21
	
Start:
	rjmp Start
	
	
loopu: lsr r18
	dec r30
	brne loopu
	ret

loopv: lsr r19
	dec r31
	brne loopv
	ret

loopw: lsr r20
	dec r29
	brne loopw
	ret

loopz: lsr r21
	dec r28
	brne loopz
	ret
	
loopf: lsl r21
	dec r28
	brne loopf
	ret
