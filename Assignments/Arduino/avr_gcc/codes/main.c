#include <avr/io.h>
#include <stdbool.h>

int main (void)
{
 bool u,v,w,z,f;
 
 DDRB = 0b00100000;
 DDRD = 0b11000011;
 PORTD = 0b00111100;
 
        while(1)
	{
	 u = (PIND & (1 << PIND2)) == (1 << PIND2);	 
	 v = (PIND & (1 << PIND3)) == (1 << PIND3);	 
	 w = (PIND & (1 << PIND4)) == (1 << PIND4);	 
	 z = (PIND & (1 << PIND5)) == (1 << PIND5);
	 
	 f = ((u||!v)&&(!w))||(z);
	
	 PORTB |= (f << 5);
	}
        return 0;
}
