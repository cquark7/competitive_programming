from sys import stdout, stdin
d = {1: 1, 2: 2, 4: 3, 8: 4, 16: 5, 30: 6, 60: 7, 96: 8, 160: 9, 270: 10, 540: 11, 792: 12, 1584: 13, 2592: 14, 4032: 15, 5376: 16, 10752: 17, 14688: 18, 29376: 19, 41040: 20, 60800: 21, 96000: 22, 192000: 23, 242880: 24, 340032: 25, 532224: 26, 677376: 27, 917280: 28, 1834560: 29, 2332800: 30, 4665600: 31, 5529600: 32, 7864320: 33, 12165120: 34, 16422912: 35, 19595520: 36, 39191040: 37, 60466176: 38, 85100544: 39, 102435840: 40, 204871680: 41, 258048000: 42, 516096000: 43, 677376000: 44, 819624960: 45, 1258709760: 46, 2517419520: 47, 2876670720: 48, 3698576640: 49, 4464046080: 50, 6210846720: 51, 8087040000: 52, 16174080000: 53, 18559756800: 54, 23984916480: 55, 28217548800: 56, 39016857600: 57, 59609088000: 58, 119218176000: 59, 137106432000: 60, 274212864000: 61, 418535424000: 62, 492139929600: 63, 543050956800: 64, 695105224704: 65, 850195906560: 66, 1700391813120: 67, 2190889451520: 68, 3012472995840: 69, 3543845437440: 70, 7087690874880: 71, 7848891187200: 72, 15697782374400: 73, 23878316851200: 74, 27450031472640: 75, 35265665433600: 76, 43662252441600: 77, 53061765120000: 78, 106123530240000: 79, 117666791424000: 80, 130387525632000: 81, 198057000960000: 82, 396114001920000: 83, 447913525248000: 84, 564371041812480: 85, 856880423239680: 86, 1169709784104960: 87, 1363487007375360: 88, 2726974014750720: 89, 3024469750579200: 90, 3703432347648000: 91, 4735710904320000: 92, 6454598565888000: 93, 9790683217920000: 94, 12282857127936000: 95, 13247091081216000: 96, 26494182162432000: 97, 30342810729185280: 98, 35148882404966400: 99, 39001250856960000: 100, 78002501713920000: 101, 93807673344000000: 102, 187615346688000000: 103, 217463242752000000: 104, 244254714259046400: 105, 369974052480614400: 106, 739948104961228800: 107, 798687560466432000: 108, 1597375120932864000: 109, 1842071925172469760: 110}
output = ''
for t in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n in d:
        output += "%d\n" % d[n]
    else:
        output += "nai\n"
stdout.write(output)
