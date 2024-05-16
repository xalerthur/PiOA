#
# Вывод программы вставить в любой онлайн-редактор диаграмм Mermaid!
#

const_Elems = [1, 2, 2, 3, 4, 5]
const_FinishValue = 12


def step( sstr: str, depth: int, cursum: int ):
	global const_FinishValue

	print( f"{sstr}(({cursum}))" )

	if ( cursum > const_FinishValue ):
		print( f"{sstr} ~~~ {sstr}X[ {cursum}>{const_FinishValue} ]:::Limit" )

	elif ( cursum == const_FinishValue ):
		#if ( depth < len( const_Elems ) ):
		#	outputseq = "+".join( map( str, const_Elems[depth : ] ) )
		#	print( f"{sstr} ~~~ {sstr}X[ {cursum}+{outputseq} > {const_FinishValue} ]:::Limit" )
		#else:
		outputseq = "'"
		for i, char in enumerate( sstr[1 : ] ):
			if ( char == 'L' ):
				outputseq += str( const_Elems[ i ] ) + ", "

		outputseq = outputseq[ : -2 ] + "'"
		print( f"{sstr} ===> {sstr}X[[ {outputseq} ]]:::Found" )

	elif ( depth >= len( const_Elems ) ):
		print( f"{sstr} ~~~ {sstr}X[ {cursum}<{const_FinishValue} ]:::Limit" )

	else:
		curelem = const_Elems[ depth ]
		print( f"{sstr} --+{curelem}--> {sstr}L" )
		step( sstr + "L", depth + 1, cursum + curelem )
		print( f"{sstr} --No {curelem}--> {sstr}R" )
		step( sstr + "R", depth + 1, cursum )


print( "flowchart TD" )
print( "classDef Limit stroke-width:0, fill:#111111, opacity:0.5" )
print( "classDef Found stroke:#0A0" )

step( "A", 0, 0 )
#print( f"Root --> L; Root --> R" )
#step( "L", 1, 0 )
#step( "R", 1, 0 )

print()


# The program should output something like this (but not in such order):
'''
flowchart TD
    Root((0))
    L((1)); R((0))
    LL((3)); LR((1))
    RL((2)); RR((0))
    LLL((6)); LLR((3))
    LRL((4)); LRR((1))
    RLL((5)); RLR((2))
    RRL((3)); RRR((0))

    Root--+1-->L; Root--Без 1-->R

    L--+2-->LL; L--Без 2-->LR
    R--+2-->RL; R--Без 2-->RR

    LL--+3-->LLL; LL--Без 3-->LLR
    LR--+3-->LRL; LR--Без 3-->LRR
    RL--+3-->RLL; RL--Без 3-->RLR
    RR--+3-->RRL; RR--Без 3-->RRR

    RLL ~~~ RLLX[5 == 5]
    RLR ~~~ RLRX[0 < 5]
'''
