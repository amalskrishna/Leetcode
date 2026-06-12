bool canConstruct(char* ransomNote, char* magazine) {
    int cnt[26]={0};

    for(int i=0;magazine[i]!='\0';i++)
        cnt[magazine[i]-'a']++;
    
    for(int i=0; ransomNote[i]!='\0';i++){
        int temp=ransomNote[i]-'a';
        if (cnt[temp]==0)
            return false;
        cnt[temp]--;
    }
    return true;

}