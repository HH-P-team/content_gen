// import './Subjects.css';
import { useState, useEffect } from 'react';
import getAllPosts from '../../api/posts/post.api';

import Card from '../Card/Card';

export default function Posts() {
    const [data, setData] = useState([]);

    useEffect(() => {
      getAllPosts().then((data) => {
        if (data.status) {
          setData(data.result);
        }
      });
    }, []);

    return (
        <div>
            <h2>Рекламные посты</h2>
            <div className="Posts">
                {data.map((elem) => <Card name={elem.name} key={elem.id} />)}
            </div>
        </div>
    );
}
