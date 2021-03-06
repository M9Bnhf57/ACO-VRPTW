import sqlite3
from statistics import mean


dtb='data_files/simPop.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

c.execute('Delete from OutZipCombs2')

c.execute(  '''
    select  comb_id,
            zip_cd1,
            zip_cd2,
            gdist,
            gtime

    from    OutZipCombs1
            ''')
recs=c.fetchall()


for rec in recs:

    if rec[3][-2:] == 'mi':
        #print(rec[3][:-2])
        dist=float(rec[3][:-2])
    else:
        dist=35
    
    ts0=rec[4].split(' ')
    
    if len(ts0)==4:
        ts1=60*int(ts0[0])+int(ts0[2])
    else:
        ts1=int(ts0[0])
    
    if int(ts1)<10:
        ts1=20
        
    c.execute('''INSERT INTO OutZipCombs2(comb_id,zip_cd1,zip_cd2,gdist,gtime,dist,tme)
            VALUES(?,?,?,?,?,?,?)''', (rec[0],rec[1],rec[2],rec[3],rec[4],dist,ts1)) 


conn.commit()
conn.close()
