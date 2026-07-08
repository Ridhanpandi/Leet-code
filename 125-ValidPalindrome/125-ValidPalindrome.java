// Last updated: 08/07/2026, 20:50:06
class Solution{
    public boolean isPalindrome(String s) {
        s=s.toLowerCase();
        s=s.replaceAll("[^a-z0-9]","");
        String reversed=new StringBuilder(s).reverse().toString();
        if(s.equals(reversed)){
            return true;
        }
        else{
            return false;
        }
    }
}