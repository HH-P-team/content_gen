// import './Subjects.css';
// import { useState, useEffect } from 'react';
// import getAllPosts from '../../api/posts/post.api';
import PageWrapper from './PageWrapper';
// import Button from '../Button/Button';

// import Card from '../Card/Card';

export default function Profile() {

    // const [data, setData] = useState([]);

    // useEffect(() => {
    //   getAllPosts().then((data) => {
    //     if (data.status) {
    //       setData(data.result);
    //     }
    //   });
    // }, []);
    
  return (
      <PageWrapper
          pageName={'Профиль'}
        //   controlElement={<Button name={'Добавить'} action={() => console.log('trololo')}/>}
          content={
              <div className="Profile">
                  {/* {data.map((elem) => <Card name={elem.name} key={elem.id} />)} */}
              </div>
          }
      />
  );
}
