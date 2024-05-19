import './Products.css';
import Section from '../Section/Section';
import getAllProducts from '../../api/products/product.api';
import PageWrapper from './PageWrapper';
import Button from '../Button/Button';
import { useState, useEffect } from 'react';

export default function Products(props) {
    const [data, setData] = useState([]);

    useEffect(() => {
        getAllProducts().then((data) => {
            if (data.status) {
                // console.log(data.result);
            }
        });
    }, []);

  return (
      <PageWrapper
          pageName={'Продукты'}
          controlElement={<Button name={'Добавить'} action={() => console.log('trololo')}/>}
          content={
              <div className="Products">
                  {props.data.map((elem) => <Section name={elem.name} key={elem.id} />)}
              </div>
          }
      />
  );
}
