
wget "https://drive.google.com/uc?export=download&id=1Q6sFC_mInD0e7WBFpQhNWJCUpXWnU1OE" -O README.md
wget "https://drive.google.com/uc?export=download&id=1Ae-Ww4kQxnh2e1zIGocUgjqi4J3RdCTZ" -O rel.emb.nre.star.npy
wget "https://drive.google.com/uc?export=download&id=1IjR42qK6hxBAfiKZ0UKoyUEJ1KuLoEVK" -O rel.emb.nre.txt
wget "https://drive.google.com/uc?export=download&id=1fP9iHUiUXcpYRXatsBoQ5LSz8Oj-nLPW" -O rel.rel.id.npy
wget "https://drive.google.com/uc?export=download&id=1wvnRcr5Slg8qELOAPObPZXVmUPCHL-oL" -O rel.rel.len.npy
wget "https://drive.google.com/uc?export=download&id=1u_iKR9rHJy61-lTXezQWXxbAZJqh4aR7" -O rel.voc.pickle
wget "https://drive.google.com/uc?export=download&id=1ardvZMb8uT4YoBfcr9TLKAWi_rFvwbWJ" -O rel.word.id.npy
wget "https://drive.google.com/uc?export=download&id=1hM-_Svj9QNTy45FFQ4jWX2u-b0Gj9_G9" -O rel.word.len.npy
wget "https://drive.google.com/uc?export=download&id=1vXkAsOWxykmzjc1x7xmtvMy_IR0DcDAH" -O word.voc.pickle

fileId=14N1-LqY70hrJ2vDWHWQib3ulkVyAMwrW
fileName=subject2relation.pickle
curl -sc cookie "https://drive.google.com/uc?export=download&id=${fileId}" > /dev/null
code="$(awk '/_warning_/ {print $NF}' cookie)"  
curl -Lb cookie "https://drive.google.com/uc?export=download&confirm=${code}&id=${fileId}" -o ${fileName} 

rm -rf cookie

fileId=1rJ3KIGOVGKxP2u-0SRvjy2wTZJBwhssT
fileName=word.emb.nre.npy
curl -sc cookie "https://drive.google.com/uc?export=download&id=${fileId}" > /dev/null
code="$(awk '/_warning_/ {print $NF}' cookie)"  
curl -Lb cookie "https://drive.google.com/uc?export=download&confirm=${code}&id=${fileId}" -o ${fileName}

rm -rf cookie 
