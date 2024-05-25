import './Posts.css';
import PageWrapper from './PageWrapper';
import Button from '../Button/Button';
import AddPostForm from "../Forms/AddPostForm";
import PostCard from '../Card/PostCard';
import { useSelector, useDispatch } from 'react-redux';

export default function Posts(props) {
    
    const posts = useSelector((state) => state.posts);
    const r_posts = posts.reverse();
    const addPostMenuState = useSelector((state) => state.addPostMenuState);
    const dispatch = useDispatch();

    const buttonTitle = addPostMenuState? 'Закрыть форму' : 'Добавить пост';

    return (
        <PageWrapper
            pageName={'Рекламные посты'}
            controlElement={<Button name={buttonTitle} action={() => dispatch({ type: 'CASE_POST_MENUSTATE', value: !addPostMenuState })}/>}
            content={
                <div className="Posts">
                    <AddPostForm data={props.data}/>
                    {r_posts.map((elem) => <PostCard 
                        name={elem.product.name}
                        description={elem.description} 
                        key={elem.id} 
                        id={elem.id} 
                        img={elem.image}
                        />)} 
                </div>
            }
        />
    );
}
