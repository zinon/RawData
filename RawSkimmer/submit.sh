# !/bin/sh

python skim.py --events ../EventSelector/EventList_periodA.txt --stream physics_Muons --name 02_11.periodA --user zenon 2>&1 | tee -a log.period.A

python skim.py --events ../EventSelector/EventList_periodB.txt --stream physics_Muons --name 02_11.periodB --user zenon 2>&1 | tee -a log.period.B

python skim.py --events ../EventSelector/EventList_periodD.txt --stream physics_Muons --name 02_11.periodD --user zenon 2>&1 | tee -a log.period.D

python skim.py --events ../EventSelector/EventList_periodG.txt --stream physics_Muons --name 02_11.periodG --user zenon 2>&1 | tee -a log.period.G

python skim.py --events ../EventSelector/EventList_periodC.txt --stream physics_Muons --name 02_11.periodC --user zenon 2>&1 | tee -a log.period.C

python skim.py --events ../EventSelector/EventList_periodE.txt --stream physics_Muons --name 02_11.periodE --user zenon 2>&1 | tee -a log.period.E


#staged A

python skim.py --events ../EventSelector/EventList_periodA.txt -r 200863 -t user.zenon.98a3cd66-adfe-4b78-bc6b-22772ad75211/ --stream physics_Muons --name 02_11.periodA --user zenon 2>&1 | tee -a log.period.A.staged

python skim.py --events ../EventSelector/EventList_periodA.txt -r 201257 -t  user.zenon.94b4d3cd-aa81-46a5-9086-0f28dfb24726/ --stream physics_Muons --name 02_11.periodA --user zenon 2>&1 | tee -a log.period.A.staged

python skim.py --events ../EventSelector/EventList_periodA.txt -r 201269 -t user.zenon.1968616d-5eab-43c8-97b1-b4916c820b90/ --stream physics_Muons --name 02_11.periodA --user zenon 2>&1 | tee -a log.period.A.staged

python skim.py --events ../EventSelector/EventList_periodA.txt -r 201120 -t user.zenon.01e26f86-08a2-408b-b9d1-6c48d1ec93f8/ --stream physics_Muons --name 02_11.periodA --user zenon 2>&1 | tee -a log.period.A.staged

#staged B

python skim.py --events ../EventSelector/EventList_periodB.txt -r 203454 -t user.zenon.b04c54f1-d5da-4fbd-a455-4006d1d06495/ --stream physics_Muons --name 02_11.periodB --user zenon 2>&1 | tee -a log.period.B.staged

python skim.py --events ../EventSelector/EventList_periodB.txt -r  203169 -t user.zenon.5b57565a-c8b6-46a1-8c78-9878fb61be86/ --stream physics_Muons --name 02_11.periodB --user zenon 2>&1 | tee -a log.period.B.staged

python skim.py --events ../EventSelector/EventList_periodB.txt -r 204442 -t user.zenon.86365525-8038-4517-b37d-87562f260610/ --stream physics_Muons --name 02_11.periodB --user zenon 2>&1 | tee -a log.period.B.staged

python skim.py --events ../EventSelector/EventList_periodB.txt -r 205112 -t user.zenon.7929c3d0-cabf-468a-b024-041f31727956/ --stream physics_Muons --name 02_11.periodB --user zenon 2>&1 | tee -a log.period.B.staged

python skim.py --events ../EventSelector/EventList_periodB.txt -r  204954 -t user.zenon.ef3ec388-d3fb-43ca-a58f-102f3236d75a/ --stream physics_Muons --name 02_11.periodB --user zenon 2>&1 | tee -a log.period.B.staged

python skim.py --events ../EventSelector/EventList_periodB.txt -r  203454 -t user.zenon.50ecd4af-521a-4dfd-9f77-384d4e60932e/ --stream physics_Muons --name 02_11.periodB --user zenon 2>&1 | tee -a log.period.B.staged

python skim.py --events ../EventSelector/EventList_periodB.txt -r 204442  -t user.zenon.04ea6684-3030-443e-b62e-7814b76c595c/ --stream physics_Muons --name 02_11.periodB --user zenon 2>&1 | tee -a log.period.B.staged

python skim.py --events ../EventSelector/EventList_periodB.txt -r 203169  -t user.zenon.cd57174a-ca5a-4155-a070-eda8ac9a8981/ --stream physics_Muons --name 02_11.periodB --user zenon 2>&1 | tee -a log.period.B.staged

python skim.py --events ../EventSelector/EventList_periodB.txt -r  204442 -t user.zenon.1e622aa3-7686-476c-afcb-bb50a9723e27/ --stream physics_Muons --name 02_11.periodB --user zenon 2>&1 | tee -a log.period.B.staged

python skim.py --events ../EventSelector/EventList_periodB.txt -r  202798 -t user.zenon.9a671f4a-a4b6-4ffc-a2a9-6f2ede5d4e34/ --stream physics_Muons --name 02_11.periodB --user zenon 2>&1 | tee -a log.period.B.staged

python skim.py --events ../EventSelector/EventList_periodB.txt -r  204726 -t user.zenon.2045d839-e03f-4a0d-93e4-126b0a21b0e8/ --stream physics_Muons --name 02_11.periodB --user zenon 2>&1 | tee -a log.period.B.staged

python skim.py --events ../EventSelector/EventList_periodB.txt -r 203335  -t user.zenon.540e1a43-6e04-4157-b3f3-3e7340d30386/ --stream physics_Muons --name 02_11.periodB --user zenon 2>&1 | tee -a log.period.B.staged

python skim.py --events ../EventSelector/EventList_periodB.txt -r 204073  -t user.zenon.5b965a76-d499-4c59-9bc9-3efd2179a756/ --stream physics_Muons --name 02_11.periodB --user zenon 2>&1 | tee -a log.period.B.staged

python skim.py --events ../EventSelector/EventList_periodB.txt -r  203336 -t user.zenon.0d9c5870-fae3-4199-94a4-2c3ac79e22df/ --stream physics_Muons --name 02_11.periodB --user zenon 2>&1 | tee -a log.period.B.staged

python skim.py --events ../EventSelector/EventList_periodB.txt -r 204026  -t user.zenon.b9928af4-c82b-4820-aada-57c789b9c076/ --stream physics_Muons --name 02_11.periodB --user zenon 2>&1 | tee -a log.period.B.staged

python skim.py --events ../EventSelector/EventList_periodB.txt -r 203454  -t user.zenon.50ecd4af-521a-4dfd-9f77-384d4e60932e/ --stream physics_Muons --name 02_11.periodB --user zenon 2>&1 | tee -a log.period.B.staged

python skim.py --events ../EventSelector/EventList_periodB.txt -r  203875 -t user.zenon.7a62e331-165f-441c-8a7c-8b5434ef4186/ --stream physics_Muons --name 02_11.periodB --user zenon 2>&1 | tee -a log.period.B.staged

python skim.py --events ../EventSelector/EventList_periodB.txt -r 204955  -t  user.zenon.749cb919-d50a-41a1-8c1c-0886d9eaa08b/ --stream physics_Muons --name 02_11.periodB --user zenon 2>&1 | tee -a log.period.B.staged

python skim.py --events ../EventSelector/EventList_periodB.txt -r  204769 -t  user.zenon.0ff7e0b2-4793-4c95-a870-2a80e7669dd2/ --stream physics_Muons --name 02_11.periodB --user zenon 2>&1 | tee -a log.period.B.staged

#staged D

python skim.py --events ../EventSelector/EventList_periodD.txt -r 207749 -t user.zenon.7ff3e2c2-12cd-4cab-a6ab-4794be29ca55/ --stream physics_Muons --name 02_11.periodD --user zenon 2>&1 | tee -a log.period.D.staged

python skim.py --events ../EventSelector/EventList_periodD.txt -r 208484 -t  user.zenon.a79f4271-4d71-4b4c-a3ce-1ea0444deaa7/ --stream physics_Muons --name 02_11.periodD --user zenon 2>&1 | tee -a log.period.D.staged

python skim.py --events ../EventSelector/EventList_periodD.txt -r 208780 -t user.zenon.bca3d9e8-634d-4f02-a9da-d5f4db804f42/ --stream physics_Muons --name 02_11.periodD --user zenon 2>&1 | tee -a log.period.D.staged

python skim.py --events ../EventSelector/EventList_periodD.txt -r 208631 -t user.zenon.81fa7728-0530-4ea0-9b66-0865822d1b2b/ --stream physics_Muons --name 02_11.periodD --user zenon 2>&1 | tee -a log.period.D.staged

python skim.py --events ../EventSelector/EventList_periodD.txt -r 207864  -t user.zenon.3870b07c-8a53-4ba3-883d-dee3fe35abd1/ --stream physics_Muons --name 02_11.periodD --user zenon 2>&1 | tee -a log.period.D.staged

python skim.py --events ../EventSelector/EventList_periodD.txt -r 207664  -t user.zenon.b2a03230-a09c-4b89-8927-e71508432df2/ --stream physics_Muons --name 02_11.periodD --user zenon 2>&1 | tee -a log.period.D.staged

python skim.py --events ../EventSelector/EventList_periodD.txt -r 208126 -t user.zenon.e78575b2-8f0d-4d17-b7b3-fdfbfecac746/ --stream physics_Muons --name 02_11.periodD --user zenon 2>&1 | tee -a log.period.D.staged

python skim.py --events ../EventSelector/EventList_periodD.txt -r 208631 -t user.zenon.81fa7728-0530-4ea0-9b66-0865822d1b2b/ --stream physics_Muons --name 02_11.periodD --user zenon 2>&1 | tee -a log.period.D.staged

python skim.py --events ../EventSelector/EventList_periodD.txt -r 207532 -t user.zenon.5b391ef0-29f6-4b04-a540-e9064abf035d/ --stream physics_Muons --name 02_11.periodD --user zenon 2>&1 | tee -a log.period.D.staged

python skim.py --events ../EventSelector/EventList_periodD.txt -r  208485 -t user.zenon.2488b722-d985-4a6b-b4e8-a1caa24ea42b/ --stream physics_Muons --name 02_11.periodD --user zenon 2>&1 | tee -a log.period.D.staged

python skim.py --events ../EventSelector/EventList_periodD.txt -r  -t  --stream physics_Muons --name 02_11.periodD --user zenon 2>&1 | tee -a log.period.D.staged

python skim.py --events ../EventSelector/EventList_periodD.txt -r  -t  --stream physics_Muons --name 02_11.periodD --user zenon 2>&1 | tee -a log.period.D.staged



#staged G

python skim.py --events ../EventSelector/EventList_periodG.txt -r 211787 -t user.zenon.294072b9-c0d6-47c3-ab93-bee7bd218c6e/ --stream physics_Muons --name 02_11.periodG --user zenon 2>&1 | tee -a log.period.G.staged

python skim.py --events ../EventSelector/EventList_periodG.txt -r 212272 -t user.zenon.72068862-b28f-412b-aff7-ba04ed64b69b/ --stream physics_Muons --name 02_11.periodG --user zenon 2>&1 | tee -a log.period.G.staged

python skim.py --events ../EventSelector/EventList_periodG.txt -r 211522 -t user.zenon.1b5f013c-d7a2-45c0-b516-439d5d0e57b6/ --stream physics_Muons --name 02_11.periodG --user zenon 2>&1 | tee -a log.period.G.staged




#staged C

python skim.py --events ../EventSelector/EventList_periodC.txt -r 206614 -t user.zenon.db6e98d6-edca-41cb-93f8-9f4034b56bb9/ --stream physics_Muons --name 02_11.periodC --user zenon 2>&1 | tee -a log.period.C.staged

python skim.py --events ../EventSelector/EventList_periodC.txt -r 206955 -t user.zenon.3eb33a7b-9eb5-46d9-a10f-2a5356087668/ --stream physics_Muons --name 02_11.periodC --user zenon 2>&1 | tee -a log.period.C.staged

python skim.py --events ../EventSelector/EventList_periodC.txt -r 206955 -t user.zenon.1d239748-eabf-458b-a002-e7277c225284/ --stream physics_Muons --name 02_11.periodC --user zenon 2>&1 | tee -a log.period.C.staged

python skim.py --events ../EventSelector/EventList_periodC.txt -r 207044 -t user.zenon.44557d31-890d-4caf-bda8-31c4573ca8ee/ --stream physics_Muons --name 02_11.periodC --user zenon 2>&1 | tee -a log.period.C.staged

python skim.py --events ../EventSelector/EventList_periodC.txt -r 206962 -t user.zenon.ae10a31b-5e85-41bf-b285-46d837d5d347/ --stream physics_Muons --name 02_11.periodC --user zenon 2>&1 | tee -a log.period.C.staged

python skim.py --events ../EventSelector/EventList_periodC.txt -r 206614 -t user.zenon.a071a774-816f-40d5-8176-d953289f0899/ --stream physics_Muons --name 02_11.periodC --user zenon 2>&1 | tee -a log.period.C.staged



#staged E

python skim.py --events ../EventSelector/EventList_periodE.txt -r 209909 -t user.zenon.33d10155-69e3-4c7e-8452-8d2d00bb1647/ --stream physics_Muons --name 02_11.periodE --user zenon 2>&1 | tee -a log.period.E.staged

python skim.py --events ../EventSelector/EventList_periodE.txt -r 209161 -t user.zenon.1c8d9cd9-c892-4169-929f-010251b8b349/ --stream physics_Muons --name 02_11.periodE --user zenon 2>&1 | tee -a log.period.E.staged

python skim.py --events ../EventSelector/EventList_periodE.txt -r  209084 -t user.zenon.e66308f0-4ad9-4a77-a473-8f319c01bf56/ --stream physics_Muons --name 02_11.periodE --user zenon 2>&1 | tee -a log.period.E.staged

python skim.py --events ../EventSelector/EventList_periodE.txt -r 209866 -t user.zenon.caead1bb-7720-4b76-bb9d-5f30b5d37f70/ --stream physics_Muons --name 02_11.periodE --user zenon 2>&1 | tee -a log.period.E.staged

python skim.py --events ../EventSelector/EventList_periodE.txt -r 209608 -t user.zenon.095ca4b8-2ce7-4e8f-b2cd-4696d66e1997/ --stream physics_Muons --name 02_11.periodE --user zenon 2>&1 | tee -a log.period.E.staged

python skim.py --events ../EventSelector/EventList_periodE.txt -r 209550 -t user.zenon.9c212be9-edec-4991-b802-60b52104cad5/ --stream physics_Muons --name 02_11.periodE --user zenon 2>&1 | tee -a log.period.E.staged

python skim.py --events ../EventSelector/EventList_periodE.txt -r  -t --stream physics_Muons --name 02_11.periodE --user zenon 2>&1 | tee -a log.period.E.staged

