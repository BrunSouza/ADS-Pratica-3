public class MergeSort implements Sorter {

    public void sort(int[] a) {
        mergeSort(a, 0, a.length - 1);
    }
    
    private void mergeSort(int[] a, int p, int r) {
        if (p < r) {             
            int q = (p + r) / 2;
            mergeSort(a, p, q);
            mergeSort(a, q + 1, r);
            merge(a, p, q, r);
        }
    }
    
    private void merge(int[] a, int p, int q, int r) {
        int n1 = q - p + 1;
        int n2 = r - q;
        int[] left = new int[n1 + 1];
        int[] right = new int[n2 + 1];
        for (int i = 0; i < n1; i++) {
            left[i] = a[p + i];        
        }
        for (int j = 0; j < n2; j++) {
            right[j] = a[q + j + 1];
        }
        left[n1] = right[n2] = Integer.MAX_VALUE;

        int i = 0;
        int j = 0;
        for (int k = p; k <= r; k++) {
            if (left[i] <= right[j]) {
                a[k] = left[i];
                i++;
            } else {
                a[k] = right[j];
                j++;
            }
        }
    }
}
