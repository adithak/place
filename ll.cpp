#include<iostream>
#include<queue>
#include<vector>
using namespace std;
struct Node{
    int d;
    struct Node *l,*r;
    Node(int d1){
        data=d1;
        left=NULL;
        right=NULL;
    }
};

void insert(struct Node* root,int key)
{
    if(root->left==NULL){root->l=new Node(key); return;}
    if(root->right==NULL){root->r=new Node(key); return;}
    if(key<=root->data){insert(root->l,key); }
    else{insert(root->r,key);}
}

int height(struct Node* root){
    if(root==NULL){
        return 0;
    }
    else{
        int l=height(root->l);
        int r=height(root->r);
        if(l>r){
            return l+1;
        }
        else{
            return r+1;
        }
    }
}
vector<int> ans;
void printlvl(struct Node* root,int lvl){
    if(root==NULL){
        return;
    }
    if(lvl==1){
        ans.push_back(root->d);
          }
    else{
        printlvl(root->l,lvl-1);
        printlvl(root->r,lvl-1);
        }
}

void lvlord(struct Node* root)
{
    int h=height(root);
    for(int i=1;i<=h;i=i+2){
        printlvl(root,i);
    }
}
struct Node* findparent(struct Node* root,int av){
    queue<struct Node*> q;
    q.push(root);
    struct Node *temp,*p;
    p=NULL;
    while(!q.empty())
    {
        temp=q.front();
        q.pop();
        if(temp->d==av){
            p=temp;
            break;
        }
        if(temp->l!=NULL){
            q.push(temp->l);
        }
        if(temp->right!=NULL){
            q.push(temp->r);
        }
    }
    return p;
}
int main()
{
    struct Node *root;
    int n;
    cin>>n;
    if(n==1){
        int val;
        cin>>val;
        cout<<val;
    }
    else{
        for(int i=0;i<n-1;i++){
            if(i==0){
                int va,l;
                cin>>va>>l;
                root=new Node(va);
                insert(root,l);
            }
            else{
                int va,l;
                cin>>va>>l;
                struct Node *p=findparent(root,va);
                if(p!=NULL){
                insert(p,l);}
                else{
                    struct Node *ll=findparent(root,l);
                    insert(ll,va);
                }
            }
        }
    }
    lvlord(root);
    for(int i=0;i<ans.size();i++){
        if(i==ans.size()-1){
            cout<<ans[i];
        }
        else{
            cout<<ans[i]<<" ";
        }
    }
    return 0;
}
