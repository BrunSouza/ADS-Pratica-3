import java.util.Arrays;


public class MedidorDeOrdenacao {

	public static final String QUICK_SORT = "quick";
	public static final String MERGE_SORT = "merge";
	public static final String COUNTING_SORT = "counting";
	
	public static int[] geraDados(int quantidade, int valorMaximo) {
		int[] dados = new int[quantidade];
		for (int i = 0; i < quantidade; i++) {
			dados[i] = (int)(Math.random() * (valorMaximo + 1));
		}
		return dados;
	}
	
	public static void main(String[] args) {
		
		if (args.length < 3) {
			System.out.println("Parametros invalidos. Uso:");
			System.out.println("java MedidorDeOrdenacao <ordenador(QUICK, MERGE, COUNTING)> <tamanho-da-entrada> <valor-maximo>");
			System.exit(1);
		}
		
		int tamanhoDaEntrada = Integer.parseInt(args[1]);
		int valorMaximo = Integer.parseInt(args[2]);
		
		Sorter ordenador = null;
		
		if (args[0].equalsIgnoreCase(QUICK_SORT)) {
			ordenador = new QuickSort();
		} else if (args[0].equalsIgnoreCase(MERGE_SORT)) {
			ordenador = new MergeSort();
		} else if (args[0].equalsIgnoreCase(COUNTING_SORT)) {
			ordenador = new CountingSort(valorMaximo);
		} else {
			System.err.println("Algoritmo invalido: " + args[0] + ". Opcoes: QUICK, MERGE, COUNTING");
			System.exit(1);
		}
		
		int[] dados = geraDados(tamanhoDaEntrada, valorMaximo);
		long tempo = System.currentTimeMillis();
		ordenador.sort(dados);
		tempo = System.currentTimeMillis() - tempo;
		System.out.println("Algoritmo TamanhoDaEntrada ValorMaximo TempoDeOrdenacao");
		System.out.println(args[0] + " " + args[1] + " " + args[2] + " " + tempo);
	}
}
