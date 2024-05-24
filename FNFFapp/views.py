from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, TeamMember
from .forms import CommentForm, PostForm


class PostList(generic.ListView):
    """
    View for displaying a list of published posts paginated
    by 6 posts per page.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    """
    View for displaying a single post along with its comments.
    Allows users to add a comment if logged in.
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Handle GET requests to display a post's details and its comments.
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )


@login_required
def post(self, request, slug, *args, **kwargs):
    """
    Handle POST requests to add a comment to a post.
    """
    if not request.user.is_staff:
        raise HttpResponseForbidden("You must be an admin to view this page")

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'comment_form': comment_form,
                'liked': liked
            },
        )


class PostLike(LoginRequiredMixin, View):
    """
    View to handle liking or unliking a post.
    Requires the user to be logged in.
    """
    def post(self, request, slug, *args, **kwargs):
        """
        Handle POST request to like or unlike a post.
        """
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class TeamMemberDetails(generic.ListView):
    """
    View to display a list of team members.
    """
    model = TeamMember
    template_name = 'about.html'
    context_object_name = 'team_members'


@login_required
def post_edit(request, slug):
    """
    View to handle editing a post.
    ONly accessible by admin users.
    """
    if not request.user.is_staff:
        raise HttpResponseForbidden("You must be an admin to view this page")

    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            image = request.FILES.get('featured_image')
            if image:
                post.featured_image = image
            form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


@login_required
def post_delete(request, slug):
    """
    View to handle deleting a post.
    ONly accessible by admin users.
    """
    if not request.user.is_staff:
        raise HttpResponseForbidden("You must be an admin to view this page")
        post = get_object_or_404(Post, slug=slug)
        post.delete()
        return redirect('home')


@login_required
def post_add(request):
    """
    View to handle adding a post.
    ONly accessible by admin users.
    """
    if not request.user.is_staff:
        raise HttpResponseForbidden("You must be an admin to view this page")
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            image = request.FILES.get('featured_image')
            if image:
                form.featured_image = image
            form.save()
            return redirect("post_detail", slug=form.instance.slug)
    else:
        form = PostForm()
    return render(request, 'post_add.html', {'form': form})


def handler403(request, exception):
    """Custom 403 page"""
    return render(request, "403.html", status=403)


def handler404(request, exception):
    """ Custom 404 page """
    return render(request, "404.html", status=404)


def handler405(request, exception):
    """ Custom 405 page """
    return render(request, "405.html", status=405)


def handler500(request):
    """ Custom 500 page """
    return render(request, "500.html", status=500)
