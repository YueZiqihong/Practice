// Ziqihong Yue
// Implementation of merge sort without recursion

# include <iostream>
using namespace std;

void printseq(double* an, int n){
    for (int i=0; i<n; ++i){
        cout<<an[i]<<" ";
    }
}

void merge(double* seq1, int length1, double* seq2, int length2, double* fs){
    // Assumption: memory is correctly allocated for seq1 and seq2
    // fs is the final sequence. It is needed because we need to make a copy
    int r1=0 ,r2= 0; int rf=0;
    while ((r1 < length1) || (r2 < length2)){
        if (r1 >= length1){
            fs[rf] = seq2[r2];
            ++rf;++r2;
        }
        else{
            if (r2 >= length2){
                fs[rf] = seq1[r1];
                ++rf;++r1;
            }
            else{
                if (seq1[r1] < seq2[r2]){
                    fs[rf] = seq1[r1];
                    ++r1;
                }
                else{
                    fs[rf] = seq2[r2];
                    ++r2;
                }
                ++rf;
            }
        }
    }
}

void merge_sort(double* seq, int length){
    for (int i=1; i<length; i*=2){
        for (int j=0; j<length; j += 2*i){
            double* temp;
            int start, middle, end;
            start = j;
            middle = min(start+i, length); // In case it is not even
            end = min(middle+i, length);
            temp = new double[end-start];
            merge(seq+start, middle-start, seq+middle, end-middle, temp);
            for (int k=0; k<end-start; ++k){
                seq[start+k] = temp[k];
            }
            delete[] temp;
        }
    }
}

int main(){
    int n;
    double* an;
    cout<<"Enter n followed by n numbers:\n";
    cin>>n;
    an = new double[n];
    for (int i=0; i<n; ++i){
        cin>>an[i];
    }
    // finished constructing the sequence
    merge_sort(an, n);
    printseq(an, n);
    return 0;
}
