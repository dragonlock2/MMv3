EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 4 4
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Device:D_Photo_ALT D?
U 1 1 60F47371
P 6350 3900
AR Path="/60F47371" Ref="D?"  Part="1" 
AR Path="/60F3A827/60F47371" Ref="D5"  Part="1" 
AR Path="/60F5AA2F/60F47371" Ref="D9"  Part="1" 
AR Path="/60F5D694/60F47371" Ref="D13"  Part="1" 
F 0 "D13" V 6300 3850 50  0000 R CNN
F 1 "D_Photo_ALT" V 6255 3820 50  0001 R CNN
F 2 "Connector_PinHeader_2.00mm:PinHeader_1x02_P2.00mm_Vertical" H 6300 3900 50  0001 C CNN
F 3 "~" H 6300 3900 50  0001 C CNN
	1    6350 3900
	0    -1   -1   0   
$EndComp
$Comp
L Device:D_Photo_ALT D?
U 1 1 60F47377
P 6050 3900
AR Path="/60F47377" Ref="D?"  Part="1" 
AR Path="/60F3A827/60F47377" Ref="D4"  Part="1" 
AR Path="/60F5AA2F/60F47377" Ref="D8"  Part="1" 
AR Path="/60F5D694/60F47377" Ref="D12"  Part="1" 
F 0 "D12" V 6000 3850 50  0000 R CNN
F 1 "D_Photo_ALT" V 5955 3820 50  0001 R CNN
F 2 "Connector_PinHeader_2.00mm:PinHeader_1x02_P2.00mm_Vertical" H 6000 3900 50  0001 C CNN
F 3 "~" H 6000 3900 50  0001 C CNN
	1    6050 3900
	0    -1   -1   0   
$EndComp
$Comp
L Device:LED D?
U 1 1 60F4737E
P 5400 3950
AR Path="/60F4737E" Ref="D?"  Part="1" 
AR Path="/60F3A827/60F4737E" Ref="D2"  Part="1" 
AR Path="/60F5AA2F/60F4737E" Ref="D6"  Part="1" 
AR Path="/60F5D694/60F4737E" Ref="D10"  Part="1" 
F 0 "D10" V 5400 3900 50  0000 R CNN
F 1 "LED" V 5348 3832 50  0001 R CNN
F 2 "Connector_PinHeader_2.00mm:PinHeader_1x02_P2.00mm_Vertical" H 5400 3950 50  0001 C CNN
F 3 "~" H 5400 3950 50  0001 C CNN
	1    5400 3950
	0    -1   -1   0   
$EndComp
$Comp
L Device:LED D?
U 1 1 60F47384
P 5700 3950
AR Path="/60F47384" Ref="D?"  Part="1" 
AR Path="/60F3A827/60F47384" Ref="D3"  Part="1" 
AR Path="/60F5AA2F/60F47384" Ref="D7"  Part="1" 
AR Path="/60F5D694/60F47384" Ref="D11"  Part="1" 
F 0 "D11" V 5700 3900 50  0000 R CNN
F 1 "LED" V 5648 3832 50  0001 R CNN
F 2 "Connector_PinHeader_2.00mm:PinHeader_1x02_P2.00mm_Vertical" H 5700 3950 50  0001 C CNN
F 3 "~" H 5700 3950 50  0001 C CNN
	1    5700 3950
	0    -1   -1   0   
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 60F4738A
P 5400 3500
AR Path="/60F4738A" Ref="#PWR?"  Part="1" 
AR Path="/60F3A827/60F4738A" Ref="#PWR036"  Part="1" 
AR Path="/60F5AA2F/60F4738A" Ref="#PWR040"  Part="1" 
AR Path="/60F5D694/60F4738A" Ref="#PWR044"  Part="1" 
F 0 "#PWR044" H 5400 3350 50  0001 C CNN
F 1 "+5V" H 5415 3673 50  0000 C CNN
F 2 "" H 5400 3500 50  0001 C CNN
F 3 "" H 5400 3500 50  0001 C CNN
	1    5400 3500
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small R?
U 1 1 60F47390
P 5400 3650
AR Path="/60F47390" Ref="R?"  Part="1" 
AR Path="/60F3A827/60F47390" Ref="R9"  Part="1" 
AR Path="/60F5AA2F/60F47390" Ref="R13"  Part="1" 
AR Path="/60F5D694/60F47390" Ref="R17"  Part="1" 
F 0 "R17" H 5459 3696 50  0000 L CNN
F 1 "150" H 5459 3605 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 5400 3650 50  0001 C CNN
F 3 "~" H 5400 3650 50  0001 C CNN
	1    5400 3650
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small R?
U 1 1 60F47396
P 5700 3650
AR Path="/60F47396" Ref="R?"  Part="1" 
AR Path="/60F3A827/60F47396" Ref="R10"  Part="1" 
AR Path="/60F5AA2F/60F47396" Ref="R14"  Part="1" 
AR Path="/60F5D694/60F47396" Ref="R18"  Part="1" 
F 0 "R18" H 5759 3696 50  0000 L CNN
F 1 "150" H 5759 3605 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 5700 3650 50  0001 C CNN
F 3 "~" H 5700 3650 50  0001 C CNN
	1    5700 3650
	1    0    0    -1  
$EndComp
Wire Wire Line
	5400 3800 5400 3750
Wire Wire Line
	5400 3550 5400 3500
$Comp
L Transistor_FET:DMG2302U Q?
U 1 1 60F4739E
P 5450 4450
AR Path="/60F4739E" Ref="Q?"  Part="1" 
AR Path="/60F3A827/60F4739E" Ref="Q2"  Part="1" 
AR Path="/60F5AA2F/60F4739E" Ref="Q3"  Part="1" 
AR Path="/60F5D694/60F4739E" Ref="Q4"  Part="1" 
F 0 "Q4" H 5654 4496 50  0000 L CNN
F 1 "DMG2302U" H 5654 4405 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 5650 4375 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMG2302U.pdf" H 5450 4450 50  0001 L CNN
	1    5450 4450
	1    0    0    -1  
$EndComp
Wire Wire Line
	5550 4250 5550 4200
$Comp
L power:GND #PWR?
U 1 1 60F473A5
P 5550 4750
AR Path="/60F473A5" Ref="#PWR?"  Part="1" 
AR Path="/60F3A827/60F473A5" Ref="#PWR037"  Part="1" 
AR Path="/60F5AA2F/60F473A5" Ref="#PWR041"  Part="1" 
AR Path="/60F5D694/60F473A5" Ref="#PWR045"  Part="1" 
F 0 "#PWR045" H 5550 4500 50  0001 C CNN
F 1 "GND" H 5555 4577 50  0000 C CNN
F 2 "" H 5550 4750 50  0001 C CNN
F 3 "" H 5550 4750 50  0001 C CNN
	1    5550 4750
	1    0    0    -1  
$EndComp
Wire Wire Line
	5550 4750 5550 4650
Wire Wire Line
	5700 3750 5700 3800
$Comp
L power:+5V #PWR?
U 1 1 60F473AD
P 5700 3500
AR Path="/60F473AD" Ref="#PWR?"  Part="1" 
AR Path="/60F3A827/60F473AD" Ref="#PWR038"  Part="1" 
AR Path="/60F5AA2F/60F473AD" Ref="#PWR042"  Part="1" 
AR Path="/60F5D694/60F473AD" Ref="#PWR046"  Part="1" 
F 0 "#PWR046" H 5700 3350 50  0001 C CNN
F 1 "+5V" H 5715 3673 50  0000 C CNN
F 2 "" H 5700 3500 50  0001 C CNN
F 3 "" H 5700 3500 50  0001 C CNN
	1    5700 3500
	1    0    0    -1  
$EndComp
Wire Wire Line
	5700 3500 5700 3550
Wire Wire Line
	5550 4200 5400 4200
Wire Wire Line
	5400 4200 5400 4100
Wire Wire Line
	5550 4200 5700 4200
Wire Wire Line
	5700 4200 5700 4100
Connection ~ 5550 4200
$Comp
L Device:R_Small R?
U 1 1 60F473B9
P 5050 4450
AR Path="/60F473B9" Ref="R?"  Part="1" 
AR Path="/60F3A827/60F473B9" Ref="R7"  Part="1" 
AR Path="/60F5AA2F/60F473B9" Ref="R11"  Part="1" 
AR Path="/60F5D694/60F473B9" Ref="R15"  Part="1" 
F 0 "R15" V 4854 4450 50  0000 C CNN
F 1 "150" V 4945 4450 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 5050 4450 50  0001 C CNN
F 3 "~" H 5050 4450 50  0001 C CNN
	1    5050 4450
	0    1    1    0   
$EndComp
$Comp
L Device:R_Small R?
U 1 1 60F473BF
P 5200 4600
AR Path="/60F473BF" Ref="R?"  Part="1" 
AR Path="/60F3A827/60F473BF" Ref="R8"  Part="1" 
AR Path="/60F5AA2F/60F473BF" Ref="R12"  Part="1" 
AR Path="/60F5D694/60F473BF" Ref="R16"  Part="1" 
F 0 "R16" H 5259 4646 50  0000 L CNN
F 1 "10k" H 5259 4555 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 5200 4600 50  0001 C CNN
F 3 "~" H 5200 4600 50  0001 C CNN
	1    5200 4600
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 60F473C5
P 5200 4750
AR Path="/60F473C5" Ref="#PWR?"  Part="1" 
AR Path="/60F3A827/60F473C5" Ref="#PWR035"  Part="1" 
AR Path="/60F5AA2F/60F473C5" Ref="#PWR039"  Part="1" 
AR Path="/60F5D694/60F473C5" Ref="#PWR043"  Part="1" 
F 0 "#PWR043" H 5200 4500 50  0001 C CNN
F 1 "GND" H 5205 4577 50  0000 C CNN
F 2 "" H 5200 4750 50  0001 C CNN
F 3 "" H 5200 4750 50  0001 C CNN
	1    5200 4750
	1    0    0    -1  
$EndComp
Wire Wire Line
	5200 4500 5200 4450
Wire Wire Line
	5200 4450 5250 4450
Wire Wire Line
	5200 4450 5150 4450
Connection ~ 5200 4450
Wire Wire Line
	5200 4750 5200 4700
Wire Wire Line
	6050 3800 6050 3750
Wire Wire Line
	6050 3750 6200 3750
Wire Wire Line
	6350 3750 6350 3800
Text HLabel 4900 4450 0    50   Input ~ 0
en
Text HLabel 6000 4150 0    50   Input ~ 0
a
Text HLabel 6300 4150 0    50   Input ~ 0
b
Text HLabel 6250 3650 2    50   Input ~ 0
adc
Wire Wire Line
	4900 4450 4950 4450
Wire Wire Line
	6200 3750 6200 3650
Wire Wire Line
	6200 3650 6250 3650
Connection ~ 6200 3750
Wire Wire Line
	6200 3750 6350 3750
Wire Wire Line
	6000 4150 6050 4150
Wire Wire Line
	6050 4150 6050 4100
Wire Wire Line
	6300 4150 6350 4150
Wire Wire Line
	6350 4150 6350 4100
$EndSCHEMATC
