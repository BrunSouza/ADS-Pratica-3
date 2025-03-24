public class QuickSort implements Sorter {

    public void sort(int[] a) {
        quickSort(a, 0, a.length - 1);
    }
    
    private void quickSort(int[] a, int p, int r) {
        if (p < r) {
            int q = partition(a, p, r);
            quickSort(a, p, q - 1);
            quickSort(a, q + 1, r);
        }
    }

    private int partition(int[] a, int p, int r) {
        int x = a[r];
        int i = p - 1; 
        for (int j = p; j <= r - 1; j++) {
            if (a[j] <= x) {
                i++;
                exchange(a, i, j);
            }
        }
        exchange(a, i + 1, r);
        return i + 1;
    }

    private void exchange(int[] a, int i, int j) {
        int aux = a[i];
        a[i] = a[j];
        a[j] = aux;
    }
}